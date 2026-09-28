# Research Paper Workspace

A shared research paper workspace that lets teams upload, organise, and query research papers using RAG (Retrieval-Augmented Generation). Answers are scored for faithfulness to the source material using RAGAS.

**Built for ResearchDen Fall 2026 Technical Project**  
Team: Shruti, Jamal, Talib | Supervisor: Sultanul Ovi

---

## Features

- Upload a PDF and ask natural language questions about it
- Answers returned with a faithfulness score (0–1) showing how grounded the answer is in the paper
- Answer relevancy score showing how well the response addresses the question
- Shared paper collection visible to all team members
- BibTeX citation generation from uploaded papers

---

## Tech Stack

| Layer        | Technology                               |
| ------------ | ---------------------------------------- |
| PDF parsing  | PyMuPDF                                  |
| Embeddings   | sentence-transformers (all-MiniLM-L6-v2) |
| Vector store | ChromaDB                                 |
| RAG pipeline | LangChain + FastAPI                      |
| Evaluation   | RAGAS (faithfulness + answer relevancy)  |
| Frontend     | Streamlit                                |
| App database | SQLite                                   |

---

## Project Structure

````
researchden-paper-workspace/
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── api/
│   │   ├── upload.py        # POST /upload — PDF ingestion
│   │   ├── ask.py           # POST /ask — RAG Q&A
│   │   └── evaluate.py      # POST /evaluate — RAGAS scoring
│   ├── pipeline/
│   │   ├── ingest.py        # PyMuPDF text extraction
│   │   ├── chunk.py         # Text chunking
│   │   ├── embed.py         # Sentence transformer embeddings
│   │   └── retrieve.py      # ChromaDB retrieval
│   ├── evaluation/
│   │   └── ragas_eval.py    # RAGAS faithfulness + relevancy
│   └── database/
│       └── models.py        # SQLite schema
├── frontend/
│   └── streamlit_app.py     # Streamlit UI
├── tests/
│   └── test_evaluation.py   # RAGAS component tests
├── requirements.txt
└── README.md

---

## How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/shrutihishruti1/researchden-paper-workspace.git
cd researchden-paper-workspace

# 2. Create and activate virtual environment
python -m venv research
research\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the FastAPI backend
TBC

# 5. In a new terminal, start the Streamlit frontend
TBC
````

---

## Evaluation Component (RAGAS)

The faithfulness evaluation component scores every answer the system produces:

- **Faithfulness (0–1):** fraction of answer claims supported by retrieved source chunks
- **Answer Relevancy (0–1):** how well the answer addresses the question asked

Both scores are returned via `POST /evaluate` and displayed in the UI alongside every answer.

---

## Status

🚧 In active development — submission deadline 20 October 2026
