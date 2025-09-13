# utils/file_reader.py

import pandas as pd
from pypdf import PdfReader
from typing import Optional
from pathlib import Path
# Base directory where our data lives
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def read_csv_summary(filename: str) -> str:
    """
    Read a CSV file and return a simple summary.
    Args:
        filename: Name of the CSV file (e.g. 'sample.csv')
    Returns:
        A string describing the file's contents.
    """
    file_path = DATA_DIR / filename
    df = pd.read_csv(file_path)
    return f"CSV file '{filename}' has {len(df)} rows and {len(df.columns)} columns."


def read_parquet_summary(filename: str) -> str:
    """
    Read a Parquet file and return a simple summary.
    Args:
        filename: Name of the Parquet file (e.g. 'sample.parquet')
    Returns:
        A string describing the file's contents.
    """
    file_path = DATA_DIR / filename
    df = pd.read_parquet(file_path)
    return f"Parquet file '{filename}' has {len(df)} rows and {len(df.columns)} columns."


def read_pdf_content(filename: str, page_limit: Optional[int] = None) -> str:
    """
    Read a PDF file and return its text content.
    Args:
        filename: Name of the PDF file (e.g. 'sample.pdf')
        page_limit: Optional limit on number of pages to read (None for all pages)
    Returns:
        A string containing the PDF's text content.
    """
    file_path = DATA_DIR / filename
    
    if not file_path.exists():
        raise FileNotFoundError(f"PDF file '{filename}' not found in data directory")
    
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            
            # Get basic info
            num_pages = len(pdf_reader.pages)
            
            # Limit pages if specified
            pages_to_read = num_pages
            if page_limit is not None:
                pages_to_read = min(page_limit, num_pages)
            
            # Extract text from pages
            text_content = []
            for page_num in range(pages_to_read):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                if text.strip():  # Only add non-empty pages
                    text_content.append(f"--- Page {page_num + 1} ---\n{text}")
            
            # Create summary
            summary = f"PDF file '{filename}' contains {num_pages} pages"
            if page_limit is not None and page_limit < num_pages:
                summary += f" (showing first {pages_to_read} pages)"
            
            # Combine summary with content
            result = f"{summary}\n\n" + "\n\n".join(text_content)
            
            return result
            
    except Exception as e:
        raise Exception(f"Error reading PDF file '{filename}': {str(e)}")


def read_pdf_summary(filename: str) -> str:
    """
    Read a PDF file and return a simple summary.
    Args:
        filename: Name of the PDF file (e.g. 'sample.pdf')
    Returns:
        A string describing the file's contents.
    """
    file_path = DATA_DIR / filename
    
    if not file_path.exists():
        raise FileNotFoundError(f"PDF file '{filename}' not found in data directory")
    
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            num_pages = len(pdf_reader.pages)
            
            # Get some metadata if available
            metadata = pdf_reader.metadata
            title = metadata.get('/Title', 'Unknown') if metadata else 'Unknown'
            author = metadata.get('/Author', 'Unknown') if metadata else 'Unknown'
            
            return f"PDF file '{filename}' has {num_pages} pages. Title: {title}, Author: {author}"
            
    except Exception as e:
        raise Exception(f"Error reading PDF file '{filename}': {str(e)}")


