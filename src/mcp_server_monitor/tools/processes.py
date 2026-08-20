"""Process monitoring tools."""

import psutil


def list_processes(filter_name: str = "", sort_by: str = "memory") -> str:
    """List running processes with optional filtering.

    Args:
        filter_name: Optional substring to filter process names (case-insensitive).
        sort_by: Sort results by 'memory', 'cpu', or 'name' (default: memory).

    Returns:
        A formatted list of running processes with their PID, name, CPU, and memory usage.
    """
    processes = []
    for proc in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        try:
            info = proc.info
            if filter_name and filter_name.lower() not in info["name"].lower():
                continue
            processes.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    sort_key = {
        "memory": lambda p: p["memory_percent"] or 0,
        "cpu": lambda p: p["cpu_percent"] or 0,
        "name": lambda p: p["name"].lower(),
    }.get(sort_by, lambda p: p["memory_percent"] or 0)

    processes.sort(key=sort_key, reverse=(sort_by != "name"))

    top = processes[:15]
    if not top:
        return f"No processes found matching filter: '{filter_name}'"

    lines = [f"Found {len(processes)} processes (showing top 15 by {sort_by}):", ""]
    lines.append(f"{'PID':<8} {'Name':<30} {'CPU%':<8} {'Memory%':<10}")
    lines.append("-" * 58)
    for p in top:
        cpu = p["cpu_percent"] or 0
        mem = p["memory_percent"] or 0
        lines.append(f"{p['pid']:<8} {p['name']:<30} {cpu:<8.1f} {mem:<10.1f}")

    return "\n".join(lines)
