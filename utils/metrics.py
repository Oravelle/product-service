import psutil


def bytes_to_gb(value: int) -> float:
    return round(value / (1024 ** 3), 2)


def sys_metrics():
  memory = psutil.virtual_memory()
  disk = psutil.disk_usage("/mnt/d")

  return {
      "cpu": {
          "usage_percent": psutil.cpu_percent(interval=1),
          "core_count": psutil.cpu_count()
      },
      "memory": {
          "total_gb": bytes_to_gb(memory.total),
          "used_gb": bytes_to_gb(memory.used),
          "available_gb": bytes_to_gb(memory.available),
          "usage_percent": memory.percent
      },
      "disk": {
          "total_gb": bytes_to_gb(disk.total),
          "used_gb": bytes_to_gb(disk.used),
          "free_gb": bytes_to_gb(disk.free),
          "usage_percent": disk.percent
      }
  }