# MCP Server Health Monitor

An MCP (Model Context Protocol) server that lets LLMs monitor server infrastructure. Connect it to OpenCode, Claude Code, or any MCP-compatible client and ask natural language questions about your server's health.

## What it does

Ask your LLM things like:
- "Is my web server responding?"
- "How much disk space do I have left?"
- "What processes are using the most memory?"
- "Is port 3306 open?"

## Tools

| Tool | Description |
|------|-------------|
| `check_http_endpoint` | Check if a URL responds with 200 OK |
| `check_disk_usage` | Get disk space info |
| `check_memory_usage` | Get RAM and swap usage |
| `check_cpu_usage` | Get CPU utilization per core |
| `check_port` | Check if a TCP port is open |
| `list_processes` | List running processes with optional filtering |

## Resources

| Resource | Description |
|----------|-------------|
| `system://info` | OS, hostname, uptime |
| `system://health` | Aggregated health status |

## Tech stack

- Python 3.12+
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) v2
- psutil (system metrics)
- httpx (HTTP checks)

## Setup

1. Install dependencies:

```shell
uv sync
```

2. Run the server:

```shell
uv run mcp-server-monitor
```

Or run directly:

```shell
uv run python -m mcp_server_monitor
```

## Testing with MCP Inspector

```shell
uv run mcp dev src/mcp_server_monitor/server.py
```

This opens the MCP Inspector in your browser where you can call tools interactively.

## Connecting to OpenCode

Add to your `opencode.json`:

```json
{
  "mcpServers": {
    "server-monitor": {
      "command": "uv",
      "args": ["run", "--project", "C:\\Users\\nikol\\Documents\\mcp-server-monitor", "mcp-server-monitor"]
    }
  }
}
```

## Running tests

```shell
uv run pytest
```

## Project structure

```
src/mcp_server_monitor/
├── __init__.py          Package metadata
├── __main__.py          Entry point
├── server.py            MCP server setup
├── tools/
│   ├── http.py          HTTP endpoint checking
│   ├── system.py        CPU, memory, disk
│   ├── network.py       Port checking
│   └── processes.py     Process listing
└── resources/
    └── status.py        System info and health
```

## License

MIT
