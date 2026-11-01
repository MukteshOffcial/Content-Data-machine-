import os

from fastmcp import FastMCP
from fastmcp.server.auth.providers.github import GitHubProvider
from fastmcp.server.dependencies import get_access_token


# Configuration
GITHUB_CLIENT_ID = os.environ["FASTMCP_SERVER_AUTH_GITHUB_CLIENT_ID"]
GITHUB_CLIENT_SECRET = os.environ["FASTMCP_SERVER_AUTH_GITHUB_CLIENT_SECRET"]

BASE_URL = os.environ.get(
    "FASTMCP_SERVER_AUTH_GITHUB_BASE_URL",
    "https://instagram-data-machine.onrender.com"
)

ALLOWED_GITHUB_USERNAME = "MukteshOfficial"


# GitHub OAuth
auth = GitHubProvider(
    client_id=GITHUB_CLIENT_ID,
    client_secret=GITHUB_CLIENT_SECRET,
    base_url=BASE_URL
)


# Create MCP server
mcp = FastMCP(
    "Instagram Data Machine",
    auth=auth
)


# Authorization check
def verify_user():
    token = get_access_token()

    if token is None:
        raise PermissionError("Authentication required.")

    username = token.claims.get("login")

    if username != ALLOWED_GITHUB_USERNAME:
        raise PermissionError(
            "Access denied. This account is not authorized."
        )

    return username


# Authentication test tool
@mcp.tool
def hello_machine() -> str:
    """
    Check Instagram Data Machine authentication and authorization.
    """

    username = verify_user()

    return (
        f"Instagram Data Machine is online. "
        f"Authenticated GitHub account: {username}"
    )


# Start server
if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8000))

    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port
    )
