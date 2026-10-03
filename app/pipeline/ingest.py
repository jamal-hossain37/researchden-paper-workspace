# app/pipeline/ingest.py
# PRIMARY OWNER: Jamal
# FALLBACK AUTHOR: Shruti (built independently to agreed interface contract)
# STATUS: Fallback active — replace with Jamal's version when delivered

import fitz  # PyMuPDF — 'fitz' is the library's internal name, imported as fitz

def ingest_pdf(file_path: str) -> str:
    """
    Extracts all text from a PDF file and returns it as a single string.

    Args:
        file_path: Path to the PDF file (e.g. "data/paper.pdf")

    Returns:
        Full text content of the PDF as one string
    """
    doc = fitz.open(file_path)
    all_text = []

    for page in doc:
        page_text = page.get_text()
        all_text.append(page_text)

    doc.close()
    return "\n".join(all_text)


if __name__ == "__main__":
    file_path = "data/Es et al. - 2025 - Ragas Automated Evaluation of Retrieval Augmented Generation.pdf"

    full_text = ingest_pdf(file_path)

    print(f"Total characters extracted: {len(full_text)}")
    print("\nFirst 500 characters:")
    print(full_text[:500])