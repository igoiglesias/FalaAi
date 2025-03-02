import psutil


class Conversoes:
    
    def __init__(self):
        pass
    
    def get_disk_usage(self) -> dict:
        disk_usage = psutil.disk_usage("/")
        total_gb = disk_usage.total / (1024 ** 3)
        used_gb = disk_usage.used / (1024 ** 3)
        free_gb = disk_usage.free / (1024 ** 3)
        percent_used = (disk_usage.used / disk_usage.total) * 100

        return {
            "total": f"{total_gb:.2f} GB",
            "usado": f"{used_gb:.2f} GB",
            "livre": f"{free_gb:.2f} GB",
            "percentual_usado": f"{percent_used:.2f}%"
        }
    
    def get_memory_usage(self) -> dict:
        mem = psutil.virtual_memory()
        total_gb = mem.total / (1024 ** 3)
        used_gb = mem.used / (1024 ** 3)
        free_gb = mem.available / (1024 ** 3)
        percent_used = mem.percent  # Percentual de uso

        return {
            "total": f"{total_gb:.2f} GB",
            "usado": f"{used_gb:.2f} GB",
            "livre": f"{free_gb:.2f} GB",
            "percentual_usado": f"{percent_used:.2f}%"
        }