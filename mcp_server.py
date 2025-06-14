"""Minimal Model Context Protocol server using FastMCP."""

from fastmcp import FastMCP

app = FastMCP(title="SK Buddy MCP Server")


@app.get("/handshake")
async def handshake():
    """Basic MCP handshake endpoint."""
    return {"mcp_version": "0.1.0", "name": app.title}


@app.get("/")
async def root():
    """Root endpoint providing a simple status message."""
    return {"message": "MCP server is running"}


def main() -> None:
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
