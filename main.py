import os
from fastmcp import FastMCP

# Create our MCP server
mcp = FastMCP("Instagram Data Machine")

# First test tool
@mcp.tool
def hello_machine() -> str:
    """
    Check whether the Instagram Data Machine is working.
    """
    return "Instagram Data Machine is online and working!"

# Start the server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port
    )
