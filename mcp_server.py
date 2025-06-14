"""Minimal Model Context Protocol server using FastMCP."""

from fastmcp import FastMCP
import pandas as pd
from pydantic import BaseModel
import uuid

app = FastMCP(title="SK Buddy MCP Server")
app.state.dataframes = {}


class LoadCSVRequest(BaseModel):
    """Request model for the load_csv tool."""

    path: str


@app.post("/load_csv")
async def load_csv(request: LoadCSVRequest) -> dict[str, list[str] | str]:
    """Load a CSV file and store the dataframe in memory under a unique ID."""
    df = pd.read_csv(request.path)
    # Generate an ID and store the dataframe in the application state
    df_id = uuid.uuid4().hex
    app.state.dataframes[df_id] = df
    return {
        "id": df_id,
        "rows": df.shape[0],
        "columns": df.columns.tolist(),
    }


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
