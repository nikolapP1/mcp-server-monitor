"""Main MCP server setup."""

from mcp.server.fastmcp import FastMCP

from .tools.http import check_http_endpoint
from .tools.system import check_cpu_usage, check_disk_usage, check_memory_usage
from .tools.network import check_port
from .tools.processes import list_processes
from .resources.status import get_system_info, get_system_health

mcp = FastMCP(
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
