# Claims Automation System

## 🚀 Overview

The Claims Automation System is an AI-powered, modular platform that accelerates insurance claim processing. It leverages intelligent document handling, automated classification, smart workflow routing, and built-in rule compliance to streamline claims from submission through adjudication. The system is ideal for insurers, TPAs, or tech consultancies seeking scalable workflow automation and rapid digital transformation.

## 🎯 Features

- **Docs Processing:** Extracts and analyzes text from claim files (images, .txt).
- **Claims Classification:** Categorizes and prioritizes claims with extendable ML logic.
- **Workflow Routing:** Dynamically assigns claims to the appropriate team or process queue.
- **Policy Compliance:** Checks claim eligibility with customizable rule sets.
- **API & UI:** RESTful FastAPI service with a modern, interactive Streamlit frontend.
- **AI-Ready:** Supports extension with RAG/LLMs for advanced extraction and decisioning[1].

## 🏗️ Project Structure

```
claims_automation_system/
├── src/
│   ├── main.py                         # FastAPI entrypoint
│   ├── document_processing/processor.py # Document parsing & OCR
│   ├── claims_classification/classifier.py # Claim type/prio logic
│   ├── workflow_optimization/router.py     # Claim assignment logic
│   └── policy_compliance/compliance.py     # Basic business rules
├── ui_app.py                           # Streamlit UI
├── requirements.txt                    # Python dependencies
└── README.md                           # Project info & guide
```

## 🚦 Quick Start

1. **Setup:**  
   Install dependencies  
   ```
   pip install -r requirements.txt
   ```
2. **Run backend:**  
   ```
   uvicorn src.main:app --reload
   ```
   By default, API runs at [http://localhost:8000](http://localhost:8000)
3. **Run UI:**  
   ```
   streamlit run ui_app.py
   ```
   UI opens at [http://localhost:8501](http://localhost:8501)

## 📥 Usage Guide

- **Upload a Claim Document** via the UI (accepts: `.png`, `.jpg`, `.jpeg`, `.txt`).
- **View Extracted Data:** OCR will pull text for further classification.
- **Review Classification & Routing:** See the type, priority, and handling path.
- **Check Policy Compliance:** Immediately know if the claim is eligible or excluded.

## 🧠 AI & Extensibility

- Core logic is modular—with clear interfaces for plugging in:
   - Document models (for PDFs, .docx, etc.)
   - ML-based classifiers or Retrieval-Augmented Generation (RAG) and LLMs[1]
   - Custom rules engines
- Ideal for rapid prototyping and integration with modern AI tools[1][2].

## 🛠️ Customization

- **Add file support:** Integrate `pdfplumber` or `python-docx` to cover more formats.
- **Upgrade classifiers:** Drop in Scikit-learn, XGBoost, or LLM modules for deeper intelligence.
- **UI/UX:** Style the Streamlit UI with custom CSS or migrate to a React/Vue frontend for further polish.

## 🤖 Tech Stack

- **Backend:** FastAPI (Python)
- **Document Processing:** Pillow, pytesseract
- **Frontend:** Streamlit
- **AI/ML-Ready:** Scikit-learn, transformers (optionally extendable)
- **Dev tools:** RAG/LLMs, modular Python utilities[1][2]

## 📄 License

This project is open for customization and internal use. For production deployments, review your company’s compliance and data protection requirements.

## 🌟 Authors & Contributions

- Led and assembled by Anish
- Contributions, feature requests, and improvements welcome—just open an issue or pull request!

