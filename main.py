import os
from fastmcp import FastMCP
from fastmcp.server.auth import StaticTokenVerifier

# Load authentication token from Render
auth_token = os.environ.get("MCP_AUTH_TOKEN")

if not auth_token:
    raise RuntimeError("MCP_AUTH_TOKEN is required")

# Configure authentication
auth = StaticTokenVerifier(
    tokens={
        auth_token: {
            "client_id": "claude",
            "scopes": [],
        }
    }
)

# Create protected MCP server
mcp = FastMCP("Instagram Data Machine", auth=auth)

# Test tool
@mcp.tool
def hello_machine() -> str:
    """
    Check whether the Instagram Data Machine is working.
    """
    return "Instagram Data Machine is online and working!"

# Start server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port
    )
