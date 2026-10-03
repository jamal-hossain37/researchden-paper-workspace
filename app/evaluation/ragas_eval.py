# app/evaluation/ragas_eval.py
# RAGAS Faithfulness Evaluation — Es et al. (2023) arXiv:2309.15217
# Evaluates whether LLM-generated answers are grounded in retrieved context

import os
from dotenv import load_dotenv, find_dotenv
from datasets import Dataset
from ragas.metrics import faithfulness
from ragas import evaluate
from langchain_google_genai import ChatGoogleGenerativeAI
from ragas.llms import LangchainLLMWrapper

# Load API key from .env file
load_dotenv(find_dotenv())

def get_ragas_llm():
    """
    Creates and returns a Gemini LLM wrapped for RAGAS use.
    Called each time evaluate_faithfulness() runs.
    """
    gemini = ChatGoogleGenerativeAI(model="gemini-3.8-flash")
    return LangchainLLMWrapper(gemini)

def evaluate_faithfulness(question: str, answer: str, contexts: list[str]) -> float:
    """
    Scores whether the answer is grounded in the retrieved contexts.
    
    Args:
        question: The user's original question
        answer: The LLM-generated answer
        contexts: List of retrieved text chunks from the document
    
    Returns:
        Faithfulness score between 0.0 and 1.0
        1.0 = fully grounded, 0.0 = fully hallucinated
    """
    ragas_llm = get_ragas_llm()
    faithfulness.llm = ragas_llm

    sample = {
        "question": [question],
        "answer": [answer],
        "contexts": [contexts],
        "ground_truth": [""]  # not used by faithfulness metric
    }

    dataset = Dataset.from_dict(sample)
    result = evaluate(dataset, metrics=[faithfulness])
    return float(result["faithfulness"][0])


# Quick test — run this file directly to verify setup
if __name__ == "__main__":

    # TEST 1 — Perfect faithfulness (score should be ~1.0)
    # Answer is fully supported by the context
    score1 = evaluate_faithfulness(
        question="What does the amygdala do?",
        answer="The amygdala processes emotional responses, especially fear.",
        contexts=["The amygdala is a brain region involved in processing emotions, particularly the fear response. It plays a key role in threat detection and emotional memory."]
    )
    print(f"Test 1 (perfect): {score1}")

    # TEST 2 — Partial faithfulness (score should be ~0.5)
    # Answer mixes one supported claim with one unsupported claim
    score2 = evaluate_faithfulness(
        question="What does the amygdala do?",
        answer="The amygdala processes fear. It also controls voluntary movement.",
        contexts=["The amygdala is a brain region involved in processing emotions, particularly the fear response."]
    )
    print(f"Test 2 (partial): {score2}")

    # TEST 3 — Low faithfulness (score should be ~0.0)
    # Answer is completely unsupported by the context
    score3 = evaluate_faithfulness(
        question="What does the amygdala do?",
        answer="The amygdala produces insulin and regulates blood sugar levels.",
        contexts=["The amygdala is a brain region involved in processing emotions, particularly the fear response."]
    )
    print(f"Test 3 (low): {score3}")