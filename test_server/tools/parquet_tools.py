# tools/parquet_tools.py

from server import mcp
from utils.file_reader import read_parquet_summary
import sys

@mcp.tool()
def summarize_parquet_file(filename: str) -> str:
    """
    Summarize a Parquet file by reporting its number of rows and columns.
    Args:
        filename: Name of the Parquet file in the /data directory (e.g., 'sample.parquet')
    Returns:
        A string describing the file's dimensions.
    """
    print("📦 Registered tool: read_parquet", file=sys.stderr)
    return read_parquet_summary(filename)