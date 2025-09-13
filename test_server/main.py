from server import mcp
import sys
import traceback

# Import tools to register them
try:
    import tools.csv_tools
    import tools.parquet_tools
    import tools.pdf_tools
    import tools.math_tools

except Exception:
    print("❌ Error importing tools:", file=sys.stderr)
    traceback.print_exc(file=sys.stderr)

print("✅ Tools imported. Starting server...", file=sys.stderr)

if __name__ == "__main__":
    try:
        mcp.run()
    except Exception:
        print("❌ MCP server crashed:", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)