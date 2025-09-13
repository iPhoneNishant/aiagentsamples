# tools/csv_tools.py

from server import mcp
from utils.file_reader import read_csv_summary
import sys

@mcp.tool()
def summarize_csv_file(filename: str) -> str:
    """
    Summarize a CSV file by reporting its number of rows and columns.
    Args:
        filename: Name of the CSV file in the /data directory (e.g., 'sample.csv')
    Returns:
        A string describing the file's dimensions.
    """
    print("📦 Registered tool: read_csv", file=sys.stderr)
    return read_csv_summary(filename)