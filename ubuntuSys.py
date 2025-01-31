import platform
import psutil
import socket
import datetime

def get_os_info():
    return {
        "OS": platform.system(),
        "Version": platform.release(),
        "Architecture": platform.architecture()[0]
    }

def get_cpu_info():
    return {
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical Processors": psutil.cpu_count(logical=True),
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
        "CPU Frequency (MHz)": psutil.cpu_freq().max
    }

def get_memory_info():
    mem = psutil.virtual_memory()
    return {
        "Total Memory (GB)": round(mem.total / 1e9, 2),
        "Used Memory (GB)": round(mem.used / 1e9, 2),
        "Memory Usage (%)": mem.percent
    }

def get_network_info():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return {
        "Hostname": hostname,
        "Local IP": local_ip
    }

def get_boot_time():
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    return {"System Boot Time": boot_time.strftime("%Y-%m-%d %H:%M:%S")}

def main():
    print("=== System Information ===")
    print(get_os_info())
    print("\n=== CPU Information ===")
    print(get_cpu_info())
    print("\n=== Memory Information ===")
    print(get_memory_info())
    print("\n=== Network Information ===")
    print(get_network_info())
    print("\n=== Boot Time ===")
    print(get_boot_time())

if __name__ == "__main__":
    main()
