# Test Server - MCP Data Processing Tools

A Model Context Protocol (MCP) server that provides tools for processing various data file formats including CSV, Parquet, and PDF files, along with basic mathematical operations.

## Overview

This project implements an MCP server using FastMCP that exposes several useful tools for data analysis and file processing. The server can be used by AI agents or other MCP clients to interact with data files and perform mathematical operations.

## Features

### Data Processing Tools
- **CSV Tools**: Summarize CSV files with row and column counts
- **Parquet Tools**: Summarize Parquet files with row and column counts  
- **PDF Tools**: 
  - Extract and read text content from PDF files
  - Summarize PDF files with page count and metadata
  - Optional page limit for large documents

### Mathematical Tools
- **Basic Arithmetic**: Addition, subtraction, multiplication, and division
- **Error Handling**: Proper division by zero protection

## Project Structure

```
test_server/
├── data/                    # Sample data files
│   ├── document.pdf        # Sample PDF file
│   ├── sample.csv          # Sample CSV file
│   ├── sample.parquet      # Sample Parquet file
│   └── sample.txt          # Sample text file
├── tools/                  # MCP tool implementations
│   ├── csv_tools.py        # CSV processing tools
│   ├── parquet_tools.py    # Parquet processing tools
│   ├── pdf_tools.py        # PDF processing tools
│   └── math_tools.py       # Mathematical operation tools
├── utils/                  # Utility functions
│   ├── file_reader.py      # File reading utilities
│   └── pdf_converter.py    # PDF conversion utilities
├── main.py                 # Main entry point
├── server.py               # MCP server configuration
├── generate_parquet.py     # Script to generate sample Parquet file
├── pyproject.toml          # Project dependencies
└── README.md               # This file
```

## Prerequisites

- Python 3.13 or higher
- pip or uv package manager

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd /path/to/test_server
   ```

2. **Install dependencies using uv (recommended):**
   ```bash
   uv sync
   ```
   
   Or using pip:
   ```bash
   pip install -e .
   ```

## Running the Server

### Method 1: Direct Python execution
```bash
python main.py
```

### Method 2: Using uv
```bash
uv run python main.py
```

### Method 3: Using the MCP CLI
```bash
mcp run python main.py
```

## Available Tools

### Data Processing Tools

#### `summarize_csv_file(filename: str) -> str`
Summarizes a CSV file by reporting its dimensions.
- **Parameters**: `filename` - Name of the CSV file in the `/data` directory
- **Example**: `summarize_csv_file("sample.csv")`

#### `summarize_parquet_file(filename: str) -> str`
Summarizes a Parquet file by reporting its dimensions.
- **Parameters**: `filename` - Name of the Parquet file in the `/data` directory
- **Example**: `summarize_parquet_file("sample.parquet")`

#### `read_pdf_file(filename: str, page_limit: int = None) -> str`
Reads and extracts text content from a PDF file.
- **Parameters**: 
  - `filename` - Name of the PDF file in the `/data` directory
  - `page_limit` - Optional limit on number of pages to read
- **Example**: `read_pdf_file("document.pdf", 5)`

#### `summarize_pdf_file(filename: str) -> str`
Summarizes a PDF file with page count and metadata.
- **Parameters**: `filename` - Name of the PDF file in the `/data` directory
- **Example**: `summarize_pdf_file("document.pdf")`

### Mathematical Tools

#### `add(a: int, b: int) -> int`
Adds two numbers together.
- **Example**: `add(5, 3)` returns `8`

#### `subtract(a: int, b: int) -> int`
Subtracts two numbers.
- **Example**: `subtract(10, 4)` returns `6`

#### `multiply(a: int, b: int) -> int`
Multiplies two numbers.
- **Example**: `multiply(3, 7)` returns `21`

#### `divide(a: int, b: int) -> str`
Divides two numbers (returns as string expression).
- **Example**: `divide(15, 3)` returns `"15/3"`
- **Error**: Raises `ValueError` if dividing by zero

## Sample Data

The project includes sample data files in the `/data` directory:
- `sample.csv` - Sample CSV data
- `sample.parquet` - Sample Parquet data (generated from CSV)
- `document.pdf` - Sample PDF document
- `sample.txt` - Sample text file

## Usage Examples

### Using with MCP Clients

Once the server is running, you can connect to it using any MCP-compatible client. The server will expose all the tools listed above for use by AI agents or other applications.

### Testing the Tools

You can test individual tools by calling them with appropriate parameters. For example:

```python
# Test CSV summarization
result = summarize_csv_file("sample.csv")
print(result)  # Output: "CSV file 'sample.csv' has X rows and Y columns."

# Test PDF reading
content = read_pdf_file("document.pdf", page_limit=2)
print(content)  # Output: PDF content with page separators

# Test math operations
result = add(10, 5)  # Returns 15
result = multiply(4, 6)  # Returns 24
```

## Dependencies

- **fastmcp** (>=2.12.3) - FastMCP framework for MCP servers
- **mcp[cli]** (>=1.14.0) - Model Context Protocol CLI tools
- **pandas** (>=2.3.2) - Data manipulation and analysis
- **pyarrow** (>=21.0.0) - Parquet file support
- **pypdf** (>=4.0.0) - PDF file processing

## Error Handling

The server includes comprehensive error handling:
- File not found errors for missing data files
- Division by zero protection in math tools
- PDF reading error handling
- General exception handling with detailed error messages

## Development

To add new tools:
1. Create a new file in the `tools/` directory
2. Import the `mcp` instance from `server.py`
3. Use the `@mcp.tool()` decorator on your functions
4. Import the new tool module in `main.py`

## Troubleshooting

- **Import errors**: Ensure all dependencies are installed using `uv sync` or `pip install -e .`
- **File not found**: Make sure data files exist in the `/data` directory
- **MCP connection issues**: Verify the server is running and accessible on the expected port
- **Python version**: Ensure you're using Python 3.13 or higher

## License

This project is part of the AI Agent Samples collection.
