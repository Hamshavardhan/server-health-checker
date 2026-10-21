
import shutil
from pathlib import Path

import psutil


def get_health_status(cpu, memory, disk):
    """Return HEALTHY or WARNING based on resource usage."""
    if cpu >= 90 or memory >= 90 or disk >= 90:
        return "WARNING"
    return "HEALTHY"


def check_server():
    """Collect system metrics and print a health report."""
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    drive = Path.cwd().anchor or "/"
    disk_usage = shutil.disk_usage(drive)
    disk = disk_usage.used / disk_usage.total * 100

    status = get_health_status(cpu, memory, disk)

    print("=== Server Health Report ===")
    print(f"CPU Usage:    {cpu:.1f}%")
    print(f"Memory Usage: {memory:.1f}%")
    print(f"Disk Usage:   {disk:.1f}%")
    print(f"Status:       {status}")


if __name__ == "__main__":
    check_server()
