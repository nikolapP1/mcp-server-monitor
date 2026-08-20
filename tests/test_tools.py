"""Tests for MCP server tools."""

from mcp_server_monitor.tools.http import check_http_endpoint
from mcp_server_monitor.tools.system import check_disk_usage, check_memory_usage, check_cpu_usage
from mcp_server_monitor.tools.network import check_port
from mcp_server_monitor.tools.processes import list_processes


def test_check_disk_usage():
    result = check_disk_usage("C:\\")
    assert "Total:" in result
    assert "Used:" in result
    assert "Free:" in result
    assert "Status:" in result


def test_check_memory_usage():
    result = check_memory_usage()
    assert "RAM Total:" in result
    assert "RAM Used:" in result
    assert "Status:" in result


def test_check_cpu_usage():
    result = check_cpu_usage(interval=0.1)
    assert "Overall usage:" in result
    assert "Physical cores:" in result
    assert "Status:" in result


def test_check_port_closed():
    result = check_port("localhost", port=1)
    assert "CLOSED" in result or "TIMEOUT" in result


def test_list_processes():
    result = list_processes()
    assert "PID" in result
    assert "Name" in result


def test_list_processes_with_filter():
    result = list_processes(filter_name="python")
    assert "Found" in result
