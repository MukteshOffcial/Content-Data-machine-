import os

from fastmcp import FastMCP
from fastmcp.server.auth.providers.github import GitHubProvider


# GitHub OAuth configuration
GITHUB_CLIENT_ID = os.environ[
    "FASTMCP_SERVER_AUTH_GITHUB_CLIENT_ID"
]

GITHUB_CLIENT_SECRET = os.environ[
    "FASTMCP_SERVER_AUTH_GITHUB_CLIENT_SECRET"
]

BASE_URL = os.environ.get(
    "FASTMCP_SERVER_AUTH_GITHUB_BASE_URL",
    "https://instagram-data-machine.onrender.com"
)


# Initialize GitHub authentication
auth = GitHubProvider(
    client_id=GITHUB_CLIENT_ID,
    client_secret=GITHUB_CLIENT_SECRET,
    base_url=BASE_URL
)


# Create MCP server
mcp = FastMCP(
    name="Instagram Data Machine",
    auth=auth
)


# Test tool
@mcp.tool
def hello_machine() -> str:
    """
    Test whether Instagram Data Machine is running.
    """

    return (
        "Instagram Data Machine is running successfully!"
    )


# Server startup
if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8000))

    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port
    )
