# SK Buddy

This repository contains a minimal [Model Context Protocol](https://github.com/openai/) server example.  The
server is bootstrapped using **FastMCP**, a lightweight extension of `FastAPI`
for MCP applications. **FastMCP** is a required dependency for running the
server.

## Running the server

Install the dependencies (`fastmcp` and `uvicorn`) and run:

```bash
python mcp_server.py
```

The server starts on `http://localhost:8000`. The `/handshake` endpoint can be
used by clients to perform the MCP handshake.
