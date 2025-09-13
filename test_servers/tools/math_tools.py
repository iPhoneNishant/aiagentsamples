from server import mcp
import sys

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers together.
    Args:
        a: First number
        b: Second number
    Returns:
        Sum of a and b
    """
    print("📦 Registered tool: add", file=sys.stderr)
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """
    Subtract two numbers.
    Args:
        a: First number
        b: Second number
    Returns:
        Difference of a and b
    """
    print("📦 Registered tool: subtract", file=sys.stderr)
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers.
    Args:
        a: First number
        b: Second number
    Returns:
        Product of a and b
    """
    print("📦 Registered tool: multiply", file=sys.stderr)
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> str:
    """
    Divide two numbers.
    Args:
        a: Dividend
        b: Divisor
    Returns:
        Division expression as string
    """
    print("📦 Registered tool: divide", file=sys.stderr)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return f"{a}/{b}"