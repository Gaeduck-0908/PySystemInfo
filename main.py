import platform
import psutil
import subprocess
import cpuinfo
import socket
from pynvml import nvmlInit, nvmlDeviceGetCount, nvmlDeviceGetHandleByIndex, nvmlDeviceGetName, nvmlDeviceGetMemoryInfo, nvmlDeviceGetUtilizationRates, nvmlShutdown

def get_motherboard_info():
    try:
        result = subprocess.check_output(['wmic', 'baseboard', 'get', 'Manufacturer,Product']).decode('utf-8')
        lines = result.strip().splitlines()
        if len(lines) >= 2:
            manufacturer, product = lines[1].split(None, 1)
            return manufacturer, product
        else:
            return None, None
    except Exception as e:
        print(f"Error occurred while getting the motherboard info: {e}")
        return None, None

def show_os_info():
    print("Operating System:", platform.system())
    print("OS version:", platform.version())
    print("OS build:", platform.release())
    print("Computer architecture:", platform.machine())
    print("Processor name:", platform.processor())

def show_cpu_info():
    print("CPU Core count:", psutil.cpu_count(logical=False))
    print("CPU Thread count:", psutil.cpu_count(logical=True))
    print("CPU Usage (%):", psutil.cpu_percent(interval=1))

def show_memory_info():
    memory_info = psutil.virtual_memory()
    print("Total RAM capacity (GB):", memory_info.total / (1024 ** 3))
    print("Available RAM capacity (GB):", memory_info.available / (1024 ** 3))

def show_disk_info():
    for partition in psutil.disk_partitions():
        if 'fixed' in partition.opts or 'rw' in partition.opts:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                print(f"Device: {partition.device}, Mount: {partition.mountpoint}, File system: {partition.fstype}, Capacity (GB): {usage.total / (1024 ** 3)}, Usage (GB): {usage.used / (1024 ** 3)}")
            except PermissionError:
                continue

def show_network_info():
    for interface, addrs in psutil.net_if_addrs().items():
        af_inet = [x for x in addrs if x.family == socket.AF_INET]
        for addr in af_inet:
            print(f"Interface: {interface}, IPv4 Address: {addr.address}")

def show_motherboard_info():
    m_board_manufacturer, m_board_product = get_motherboard_info()
    if m_board_manufacturer is not None and m_board_product is not None:
        print("Motherboard manufacturer:", m_board_manufacturer)
        print("Motherboard model:", m_board_product)
    else:
        print("Motherboard information not available.")

def show_processor_info():
    cpu_info = cpuinfo.get_cpu_info()
    print("Processor manufacturer:", cpu_info.get('vendor_id_raw', 'Unknown'))
    print("Processor model:", cpu_info.get('brand_raw', 'Unknown'))


def show_gpu_info():
    try:
        nvmlInit()
        device_count = nvmlDeviceGetCount()
        for i in range(device_count):
            handle = nvmlDeviceGetHandleByIndex(i)
            device_name = nvmlDeviceGetName(handle).decode('utf-8')
            memory_info = nvmlDeviceGetMemoryInfo(handle)
            utilization = nvmlDeviceGetUtilizationRates(handle)

            print(f"------ Graphics card {i + 1} ------")
            print(f"Model: {device_name}")
            print(f"Total memory (MB): {memory_info.total // (1024 ** 2)}")
            print(f"Used memory (MB): {memory_info.used // (1024 ** 2)}")
            print(f"GPU usage (%): {utilization.gpu}%")
            print(f"Memory usage (%): {utilization.memory}%")
        nvmlShutdown()

    except Exception as e:
        print(f"Error occurred while getting graphics card info: {e}")

def print_system_info():
    print("OS information:")
    show_os_info()
    print("\nCPU information:")
    show_cpu_info()
    print("\nMemory information:")
    show_memory_info()
    print("\nDisk information:")
    show_disk_info()
    print("\nNetwork information:")
    show_network_info()
    print("\nMotherboard information:")
    show_motherboard_info()
    print("\nProcessor information:")
    show_processor_info()
    print("\nGraphics card information:")
    show_gpu_info()

if __name__ == "__main__":
    print_system_info()
