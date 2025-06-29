# Data Analysis

Usefull flow for fast exploration and PoC:

- 1. **Python** (pandas, numpy)

- 2. **Exploratory Data Analysis (EDA):**
  - Plotly
  - Seaborn

- 3. **Data Preprocessing:**
  - Pydantic (type enforcement and validation)
  - Data Augmentation / Feature Crafting (optionally ask the advanced-technical desired LLM for brainstorming on feature crafting + selection; we recommend o3 / DeepSeek on June, 2025)
  - Split Train/Test/Validation

- 4. **Machine Learning:**
  - Keras / TensorFlow
  - PyTorch
  - Approach? Small scale alternatives on the test dataset

- 5. **Statistical Validation:**
  - Training and KPIs visualization (loss, performance vs [test, train])
  - k-Fold Cross Validation
  - Hypothesis tests (scipy.stats, statsmodels)

- 6. **Result Visualization:**
  - Plotly
  - Seaborn


**Inspiration / Examples:**

- [AI-Scientist](https://github.com/SakanaAI/AI-Scientist)
- [AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2)
