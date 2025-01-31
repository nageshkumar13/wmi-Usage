import os
import platform
import psutil
import shutil
import socket

# OS Information
print(f"OS Name: {platform.system()} {platform.release()}")
print(f"Version: {platform.version()}")
print(f"Architecture: {platform.architecture()[0]}")

# List Running Processes
print("\nRunning Processes:")
for proc in psutil.process_iter(attrs=['pid', 'name']):
    print(f"Process ID: {proc.info['pid']}, Name: {proc.info['name']}")

# Check CPU Usage
print(f"\nCPU Load: {psutil.cpu_percent(interval=1)}%")

# Get Disk Information
print("\nDisk Information:")
for part in psutil.disk_partitions():
    if part.fstype:  # Only consider mounted partitions
        usage = psutil.disk_usage(part.mountpoint)
        print(f"Drive: {part.device}, Free Space: {usage.free / 1e9:.2f} GB, "
              f"Total Size: {usage.total / 1e9:.2f} GB")

# Retrieve Network Adapter Information
print("\nNetwork Information:")
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(f"Hostname: {hostname}")
print(f"Local IP Address: {local_ip}")

# Get all network interfaces and IP addresses
for interface, addrs in psutil.net_if_addrs().items():
    for addr in addrs:
        if addr.family == socket.AF_INET:  # IPv4 addresses only
            print(f"Adapter: {interface}, IP Address: {addr.address}")
