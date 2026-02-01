# Translations of text exploration
=======================================================


Project Description
---
The objective of the project is to explore different exploration approaches. Use the Automatic metrics to understand to gauge the approaches.
We try to use the news commentary corpus to understand the different approaches to translation. The language should be german to english.


Local Setup
---

Getting Started
Install dependencies:

```
uv sync
```

Note: For research purposes, you can install all dependencies using:
```
uv sync --all-groups
```
For more information on uv , [uv-docs](https://docs.astral.sh/uv/).

Streamlit deployment
---
1. Run the Streamlit application:
```streamlit run app.py```
2. Open the browser and go to http://localhost:8501/ to see the application.
3. The application is now running locally.


LLM Used
---
The project uses the following LLMs:
- Model: eurollm-9b-q8_0.gguf
- Format: GGUF (quantized, 8-bit)
- Source: Triangle104/EuroLLM-9B-Q8_0-GGUF on Hugging Face