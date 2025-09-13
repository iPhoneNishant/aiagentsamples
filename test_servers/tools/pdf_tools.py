# tools/pdf_tools.py

from server import mcp
from utils.file_reader import read_pdf_content, read_pdf_summary
import sys

@mcp.tool()
def read_pdf_file(filename: str, page_limit: int = None) -> str:
    """
    Read and extract text content from a PDF file.
    Args:
        filename: Name of the PDF file in the /data directory (e.g., 'sample.pdf')
        page_limit: Optional limit on number of pages to read (None for all pages)
    Returns:
        A string containing the PDF's text content with page separators.
    """
    print("📦 Registered tool: read_pdf_file", file=sys.stderr)
    return read_pdf_content(filename, page_limit)

@mcp.tool()
def summarize_pdf_file(filename: str) -> str:
    """
    Summarize a PDF file by reporting its number of pages and metadata.
    Args:
        filename: Name of the PDF file in the /data directory (e.g., 'sample.pdf')
    Returns:
        A string describing the file's basic information.
    """
    print("📦 Registered tool: summarize_pdf_file", file=sys.stderr)
    return read_pdf_summary(filename)
