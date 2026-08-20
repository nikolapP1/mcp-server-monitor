"""Main MCP server setup."""

import sys
from pathlib import Path

src_dir = str(Path(__file__).parent / "src")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from mcp.server import MCPServer

from mcp_server_monitor.tools.http import check_http_endpoint
from mcp_server_monitor.tools.system import check_cpu_usage, check_disk_usage, check_memory_usage
from mcp_server_monitor.tools.network import check_port
from mcp_server_monitor.tools.processes import list_processes
from mcp_server_monitor.resources.status import get_system_info, get_system_health

mcp = MCPServer(
    "Server Health Monitor",
    instructions="A server health monitoring tool. Use it to check HTTP endpoints, system resources (CPU, memory, disk), network ports, and running processes.",
)

mcp.tool()(check_http_endpoint)
mcp.tool()(check_disk_usage)
mcp.tool()(check_memory_usage)
mcp.tool()(check_cpu_usage)
mcp.tool()(check_port)
mcp.tool()(list_processes)

mcp.resource("system://info")(get_system_info)
mcp.resource("system://health")(get_system_health)


def main():
    mcp.run()


if __name__ == "__main__":
    main()
