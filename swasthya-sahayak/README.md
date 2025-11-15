# SwasthyaSahayak

Multi-agent healthcare assistant for small clinics. This repository contains a production-style layout for the Capstone project: symptom triage, image assessment, and inventory forecasting agents.

**Contents**:
- `swasthya/` - package source
- `notebooks/` - demo notebook (mocked LLM for offline runs)
- `tests/` - unit tests
- `data/` - sample data
- `scripts/` - helper scripts

## Quickstart (local)

1. Create a virtual environment and install requirements:
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. Run demo notebook (Jupyter) or open `notebooks/capstone_demo.ipynb` in Kaggle/Colab.

3. Replace `swasthya/tools/mock_llm.py` with your real ADK/Gemini integration before deploying (do not commit API keys).

## Notes for Kaggle submission
- You can use the notebook for your Kaggle writeup. The notebook uses a `MockLLM` to be runnable offline.
- For bonus points, include a short demo video and optionally deploy agents to Cloud Run/Agent Engine.