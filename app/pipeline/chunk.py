# app/pipeline/chunk.py
# PRIMARY OWNER: Jamal
# FALLBACK AUTHOR: Shruti (built independently to agreed interface contract)
# STATUS: Fallback active — replace with Jamal's version when delivered

from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(full_text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """
    Splits a long text string into smaller overlapping chunks.

    Args:
        full_text:   The complete text extracted from a PDF
        chunk_size:  Maximum characters per chunk (default 500)
        overlap:     Characters shared between consecutive chunks (default 50)

    Returns:
        List of text chunk strings
    """
    # Create the splitter with our size settings
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )

    # Split the text — returns a list of strings
    chunks = splitter.split_text(full_text)

    return chunks


if __name__ == "__main__":
    # Test using the ingest module we just built
    from app.pipeline.ingest import ingest_pdf

    file_path = "data/Es et al. - 2025 - Ragas Automated Evaluation of Retrieval Augmented Generation.pdf"

    # Step 1: ingest the PDF
    full_text = ingest_pdf(file_path)
    print(f"Total characters: {len(full_text)}")

    # Step 2: chunk the text
    chunks = chunk_text(full_text)
    print(f"Total chunks created: {len(chunks)}")
    print(f"\nFirst chunk:\n{chunks[0]}")
    print(f"\nSecond chunk:\n{chunks[1]}")