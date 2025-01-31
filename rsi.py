import wmi

c = wmi.WMI()
for os in c.Win32_OperatingSystem():
    print(f"OS Name: {os.Name}")
    print(f"Version: {os.Version}")
    print(f"Manufacturer: {os.Manufacturer}")
    print(f"Architecture: {os.OSArchitecture}")


#List Running Processes
for process in c.Win32_Process():
    print(f"Process ID: {process.ProcessId}, Name: {process.Name}")


#Code to Check CPU Usage


# Iterate through all processors and get their load percentage
for cpu in c.Win32_Processor():
    print(f"CPU Load: {cpu.LoadPercentage}%")  # Print the CPU load as a percentage

#Code to Get Disk Information


# Iterate through all logical disks of type 3 (fixed/local disk)
for disk in c.Win32_LogicalDisk(DriveType=3):
    # Print the drive ID, free space (converted to GB), and total size (converted to GB)
    print(f"Drive: {disk.DeviceID}, Free Space: {int(disk.FreeSpace)/1e9:.2f} GB, \
Total Size: {int(disk.Size)/1e9:.2f} GB")    
    

#Code to Retrieve Network Adapter Information
    
# Iterate through all network adapters with IP enabled
for adapter in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
    # Print the adapter description
    print(f"Adapter: {adapter.Description}")
    # Print the first IP address associated with the adapter
    print(f"IP Address: {adapter.IPAddress[0]}")
    # Print the MAC address of the adapter
    print(f"MAC Address: {adapter.MACAddress}")    
    