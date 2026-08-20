"""System resource monitoring tools."""

import psutil


def check_disk_usage(path: str = "/") -> str:
    """Check disk usage for a given path.

    Args:
        path: The filesystem path to check (default: /).

    Returns:
        Disk usage summary with total, used, free space and percentage.
    """
    usage = psutil.disk_usage(path)
    total_gb = round(usage.total / (1024**3), 2)
    used_gb = round(usage.used / (1024**3), 2)
    free_gb = round(usage.free / (1024**3), 2)
    percent = usage.percent
    status = "critical" if percent > 90 else "warning" if percent > 80 else "healthy"
    return (
        f"Path: {path}\n"
        f"Status: {status}\n"
        f"Total: {total_gb} GB\n"
        f"Used: {used_gb} GB ({percent}%)\n"
        f"Free: {free_gb} GB"
    )


def check_memory_usage() -> str:
    """Check current memory (RAM and swap) usage.

    Returns:
        Memory usage summary with total, available, used space and percentages.
    """
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    total_gb = round(mem.total / (1024**3), 2)
    available_gb = round(mem.available / (1024**3), 2)
    used_gb = round(mem.used / (1024**3), 2)
    status = "critical" if mem.percent > 90 else "warning" if mem.percent > 80 else "healthy"
    return (
        f"Status: {status}\n"
        f"RAM Total: {total_gb} GB\n"
        f"RAM Used: {used_gb} GB ({mem.percent}%)\n"
        f"RAM Available: {available_gb} GB\n"
        f"Swap Total: {round(swap.total / (1024**3), 2)} GB\n"
        f"Swap Used: {round(swap.used / (1024**3), 2)} GB ({swap.percent}%)"
    )


def check_cpu_usage(interval: float = 1.0) -> str:
    """Check current CPU usage.

    Args:
        interval: Sampling interval in seconds (default: 1).

    Returns:
        CPU usage summary with overall percentage, core count, and per-core usage.
    """
    overall = psutil.cpu_percent(interval=interval)
    physical_cores = psutil.cpu_count(logical=False)
    logical_cores = psutil.cpu_count(logical=True)
    per_core = psutil.cpu_percent(interval=0.1, percpu=True)
    status = "critical" if overall > 90 else "warning" if overall > 80 else "healthy"
    per_core_str = ", ".join(f"{i}: {p}%" for i, p in enumerate(per_core))
    return (
        f"Status: {status}\n"
        f"Overall usage: {overall}%\n"
        f"Physical cores: {physical_cores}\n"
        f"Logical cores: {logical_cores}\n"
        f"Per-core: [{per_core_str}]"
    )
