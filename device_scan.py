import platform
import psutil

def device_scan():

    result = {}

    result["os"] = platform.system()

    result["cpu_usage"] = psutil.cpu_percent()

    result["ram_usage"] = psutil.virtual_memory().percent

    result["open_ports"] = len(psutil.net_connections())

    return result