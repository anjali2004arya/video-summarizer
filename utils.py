# utils.py

from typing import Callable

def chunked_summarize(
    text: str,
    chunk_size: int = 1000,
    summarize_func: Callable[[str], str] = None
) -> str:
    """
    Splits the input text into chunks and applies a summarization function to each chunk.

    :param text: The full input text to summarize.
    :param chunk_size: Max characters per chunk.
    :param summarize_func: Function to summarize a single chunk.
    :return: Concatenated summaries of all chunks.
    """
    if summarize_func is None:
        summarize_func = summarize  # Use default dummy summarizer

    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    summaries = [summarize_func(chunk) for chunk in chunks]
    return "\n".join(summaries)

def summarize(text: str) -> str:
    """
    Dummy summarizer that returns the first sentence or first 100 characters.
    Replace with a real summarization model as needed.
    """
    return text[:100] + "..."
