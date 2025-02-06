import psutil
import csv
import time
from datetime import datetime
import os

# Define the output CSV file
csv_filename = "system_performance.csv"

# CSV Headers
headers = [
    "Timestamp",
    "CPU_Usage(%)",
    "Memory_Usage(%)",
    "Total_Memory(MB)",
    "Available_Memory(MB)",
    "Used_Memory(MB)",
    "Swap_Usage(%)",
    "Disk_Usage(%)",
    "Disk_Read_Bytes",
    "Disk_Write_Bytes",
    "Network_Bytes_Sent",
    "Network_Bytes_Received",
    "System_Load_1m",
    "System_Load_5m",
    "System_Load_15m",
    "Top_Process_CPU",
    "Top_Process_Memory"
]

# Check if the file exists, if not, create it and add headers
if not os.path.exists(csv_filename):
    with open(csv_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

# Monitoring Loop
while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=0)

    # Memory Usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    total_memory = memory.total // (1024 * 1024)  # Convert bytes to MB
    available_memory = memory.available // (1024 * 1024)
    used_memory = memory.used // (1024 * 1024)

    # Swap Usage
    swap = psutil.swap_memory()
    swap_usage = swap.percent

    # Disk Usage
    disk = psutil.disk_usage("/")
    disk_usage = disk.percent

    # Disk I/O
    disk_io = psutil.disk_io_counters()
    disk_read_bytes = disk_io.read_bytes
    disk_write_bytes = disk_io.write_bytes

    # Network Usage
    net_io = psutil.net_io_counters()
    network_bytes_sent = net_io.bytes_sent
    network_bytes_received = net_io.bytes_recv

    # System Load
    load_avg = psutil.getloadavg()
    load_1m, load_5m, load_15m = load_avg

    # Top Process (CPU)
    top_process_cpu = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']), key=lambda p: p.info['cpu_percent'], reverse=True)[:1]
    top_process_cpu_info = f"{top_process_cpu[0].info['name']} (PID: {top_process_cpu[0].info['pid']}, CPU: {top_process_cpu[0].info['cpu_percent']}%)" if top_process_cpu else "N/A"

    # Top Process (Memory)
    top_process_memory = sorted(psutil.process_iter(['pid', 'name', 'memory_percent']), key=lambda p: p.info['memory_percent'], reverse=True)[:1]
    top_process_memory_info = f"{top_process_memory[0].info['name']} (PID: {top_process_memory[0].info['pid']}, Mem: {top_process_memory[0].info['memory_percent']}%)" if top_process_memory else "N/A"

    # Append data to CSV (Do not overwrite)
    with open(csv_filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            timestamp, cpu_usage, memory_usage, total_memory, available_memory, used_memory, swap_usage,
            disk_usage, disk_read_bytes, disk_write_bytes, network_bytes_sent, network_bytes_received,
            load_1m, load_5m, load_15m, top_process_cpu_info, top_process_memory_info
        ])

    print(f"[{timestamp}] Data logged successfully.")
    
    # Sleep before next log entry (Adjust interval as needed)
    time.sleep(0)  # Logs every 5 seconds
