# SK Buddy

This repository contains a minimal [Model Context Protocol](https://github.com/openai/) server example.  The
server is bootstrapped using **FastMCP**, a lightweight extension of `FastAPI`
for MCP applications. **FastMCP** is a required dependency for running the
server.

## Running the server

Install the dependencies listed in `requirements.txt` and run:

```bash
pip install -r requirements.txt
python mcp_server.py
```

The server starts on `http://localhost:8000`. The `/handshake` endpoint can be
used by clients to perform the MCP handshake.

## Loading CSV files

The `/load_csv` endpoint accepts a JSON body with a `path` field pointing to a
CSV file. The server loads the file using Pandas and stores the resulting
`DataFrame` in memory. Each loaded file is kept under a unique ID, which is
returned in the response:

```bash
curl -X POST -H "Content-Type: application/json" \
    -d '{"path": "data/example.csv"}' \
    http://localhost:8000/load_csv
# => {"id": "<hash>", "rows": 10, "columns": ["A", "B"]}
```
