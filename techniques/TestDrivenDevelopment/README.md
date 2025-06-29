# Test Driven Development with LLMs - A Robust Software Engineering Methodology Proposal

## 1. Define the Problem and Objectives

> **Example:**  
> _Design a logging system for a website using Python._

---

## 2. Specify Constraints at a Low Level

- **Robustness:** The method must protect the system from malicious users.
- **Access:** Legitimate users must be able to log in and perform intended actions.
- **Security:** Prevent any form of information exfiltration.
- **Extra:** Consider compliance, auditability, and privacy.

---

## 3. Break Down the Problem Into Sub-Problems

Decompose the project into logically coherent, manageable parts (e.g., authentication, logging, storage, user feedback).

---

## 4. For Each Subproblem:  
**a. Generate Tests (with Explanations):**

- Use multiple LLMs in parallel, each one proposing test cases and explaining their rationale as comments.
- **Important notes:**
    - **Threat modeling:** What would a bad actor try?
    - **Auto-fuzzing:** Integrate Hypothesis for fuzz testing.
    - **Strong typing:** Use Pydantic models (with internal validation functions).
    - Comment thoroughly to explain the intent behind each test.

---

## 5. Generate Solutions (with Explanations)

- For each subproblem, prompt a new LLM instance (can parallelize here too) to generate a solution based solely on the goals and constraints.
- Require detailed, commented code explaining the logic behind decisions.

---

## 6. Validate the Solution Against the Tests

- Run all test cases.
- Document which ones pass and which ones fail.
- Make failure explicit and add related (potentially useful) context / behavioural description (don't just "retry" blindly).

---

## 7. Iterate or Accept

- **If the solution passes:** move to integration (step 8).
- **If not, but directionally correct:**  
  - Carefully read the LLM’s code and reasoning.
  - Provide the LLM with **feedback**: summarize what fails, using input/output descriptions (not just raw test code).
  - Encourage the LLM to “think aloud” and debug via explanations and, if needed, via print/debug statements.
- Loop steps 5–7 as needed.

---

## 8. Integration: Directed Graph of Subsolutions

- Collect all subproblem function interfaces (inputs/outputs).
- Define an integration subproblem:  
  - Combine the subcomponents into a directed acyclic graph that achieves your overall goals.
- Apply the same [steps 1–7] to this "subproblem" - Integration.

---

## Potential Problems & Solutions

1. **Tests are not exhaustive:**  
   - Some edge cases remain uncovered.
   - **Solution:** Manual review, repeated iteration, and explicit aim for test coverage completeness.

2. **Circular validation (LLMs reviewing LLMs):**  
   - **Solution:** Use adversarial review—have multiple LLMs critique each other's outputs and tests.

---

## 🎉 Congratulations:  
You have engineered robust software with LLM collaboration!
