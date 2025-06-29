"""
# multi_model_consensus_openrouter.py

Example pipeline using OpenRouter for multimodel easy orchestration
"""

import os
import asyncio
import json
from typing import List, Dict

import httpx

# Load your OpenRouter API key from environment
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise RuntimeError("Please set the OPENROUTER_API_KEY environment variable.")

# Base URL for the OpenRouter API
OPENROUTER_BASE_URL = "https://api.openrouter.ai/v1/chat/completions"


# ----------- Core pipeline functions -----------

async def call_model(model_name: str, prompt: str) -> str:
    """
    Calls an LLM via OpenRouter.
    Model names must match OpenRouter's supported models, e.g.:
    'gpt-4o', 'google/vertexai-gecko-1', 'anthropic/claude-3.5'
    """
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 1024
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(OPENROUTER_BASE_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        # Assuming standard OpenAI-like response format
        return data["choices"][0]["message"]["content"]


async def gather_responses(models: List[str], prompt: str) -> Dict[str, str]:
    """
    Send the same prompt to all models in parallel and collect responses.
    """
    tasks = [call_model(m, prompt) for m in models]
    results = await asyncio.gather(*tasks)
    return dict(zip(models, results))

def summarize_responses(responses: Dict[str, str]) -> str:
    """
    Create a combined summary of all model responses.
    """
    summary = "## Modelo Responses Summary\n\n"
    for model, resp in responses.items():
        summary += f"### {model}\n{resp}\n\n"
    return summary

def build_adversarial_prompt(target_model: str, summary: str) -> str:
    """
    Construct a prompt to ask `target_model` to critique the summary.
    """
    return (
        f"{summary}\n\n"
        "Por favor, revisa críticamente los puntos anteriores y señala "
        "dónde podrían estar equivocados o incompletos, "
        "ofreciendo contraargumentos."
    )

async def adversarial_review(models: List[str], summary: str) -> Dict[str, str]:
    """
    Perform adversarial review: each model critiques the summary.
    """
    tasks = [call_model(m, build_adversarial_prompt(m, summary)) for m in models]
    results = await asyncio.gather(*tasks)
    return dict(zip(models, results))

def compute_consensus(initial: Dict[str, str], reviews: Dict[str, str], threshold: float = 0.6) -> List[str]:
    """
    Naive consensus: select statements that appear (substring match)
    in at least `threshold` fraction of combined texts.
    """
    all_texts = list(initial.values()) + list(reviews.values())
    # Split into lines for simplicity
    statements = {line.strip() for text in all_texts for line in text.split('\n') if line.strip()}
    consensus = []
    for stmt in statements:
        count = sum(stmt in text for text in all_texts)
        if count / len(all_texts) >= threshold:
            consensus.append(stmt)
    return consensus

def log_decision(initial: Dict[str, str], reviews: Dict[str, str], consensus: List[str], filename: str = "decisions_log.json"):
    """
    Save the negotiation log to a JSON file for audit and review.
    """
    log = {
        "initial_responses": initial,
        "adversarial_reviews": reviews,
        "consensus": consensus
    }
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(log, f, ensure_ascii=False, indent=2)



async def run_pipeline(models: List[str], problem: str, threshold: float = 0.6):
    
    # Stage 1: Gather initial responses
    initial = await gather_responses(models, problem)

    # Stage 2: Summarize
    summary = summarize_responses(initial)

    # Stage 3: Adversarial review
    reviews = await adversarial_review(models, summary)

    # Stage 4: Compute consensus
    consensus = compute_consensus(initial, reviews, threshold)

    # Stage 5: Logging
    log_decision(initial, reviews, consensus, filename="decisions_openrouter.json")

    return consensus

# ----------- Example usage -----------

if __name__ == "__main__":
    models = [
        "gpt-4o",                   # OpenAI's GPT-4o via OpenRouter
        "google/vertexai-gecko-1",  # Gemini-like
        "anthropic/claude-3.5",     # Claude
        "deepseek/deepseek-1",      # Hypothetical DeepSeek model
        "qwen/qwen-7b"              # Qwen
    ]
    problem_description = (
        "Define la estrategia de enrutamiento en un sistema multiagente que comparta contexto "
        "y alcance consenso sobre la acción a ejecutar."
    )
    consensus = asyncio.run(run_pipeline(models, problem_description))
    print("\n✅ Consenso final:\n")
    for stmt in consensus:
        print(f"- {stmt}")