"""System status resources."""

import platform
import time

import psutil


def get_system_info() -> str:
    """Get basic system information.

    Returns:
        System details including OS, hostname, uptime, and Python version.
    """
    uptime_seconds = time.time() - psutil.boot_time()
    days = int(uptime_seconds // 86400)
    hours = int((uptime_seconds % 86400) // 3600)
    minutes = int((uptime_seconds % 3600) // 60)

    return (
        f"Hostname: {platform.node()}\n"
        f"OS: {platform.system()} {platform.release()}\n"
        f"Architecture: {platform.machine()}\n"
        f"Python: {platform.python_version()}\n"
        f"Uptime: {days}d {hours}h {minutes}m"
    )


def get_system_health() -> str:
    """Get an aggregated health summary of the system.

    Returns:
        A combined health report covering CPU, memory, and disk.
    """
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\")

    issues = []
    if cpu > 90:
        issues.append(f"CPU critical at {cpu}%")
    elif cpu > 80:
        issues.append(f"CPU warning at {cpu}%")

    if mem.percent > 90:
        issues.append(f"Memory critical at {mem.percent}%")
    elif mem.percent > 80:
        issues.append(f"Memory warning at {mem.percent}%")

    if disk.percent > 90:
        issues.append(f"Disk critical at {disk.percent}%")
    elif disk.percent > 80:
        issues.append(f"Disk warning at {disk.percent}%")

    overall = "healthy" if not issues else "degraded" if len(issues) == 1 else "critical"

    lines = [
        f"Overall: {overall}",
        f"CPU: {cpu}%",
        f"Memory: {mem.percent}%",
        f"Disk: {disk.percent}%",
    ]
    if issues:
        lines.append("")
        lines.append("Issues:")
        for issue in issues:
            lines.append(f"  - {issue}")

    return "\n".join(lines)
