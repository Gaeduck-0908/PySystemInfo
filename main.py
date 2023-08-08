import platform
import psutil
import subprocess
import cpuinfo
import socket
import GPUtil

# get_motherboard_info
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

# get_os_info
def get_platform_system():
    return platform.system()
def get_platform_version():
    return platform.version()
def get_platform_release():
    return platform.release()
def get_platform_machine():
    return platform.machine()
def get_platform_processor():
    return platform.processor()

# get_cpu_info
def get_cpu_core():
    return psutil.cpu_count(logical=False)
def get_cpu_thread():
    return psutil.cpu_count(logical=True)
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

# get_memory_info
def get_total_ram():
    return (psutil.virtual_memory() / (1024 ** 3))
def get_available_ram():
    return (psutil.virtual_memory().available / (1024 ** 3))

# get_disk_info
def get_device_info():
    for partition in psutil.disk_partitions():
        if 'fixed' in partition.opts or 'rw' in partition.opts:
            try:
                return partition.device
            except PermissionError:
                continue
def get_mount_info():
    for partition in psutil.disk_partitions():
        if 'fixed' in partition.opts or 'rw' in partition.opts:
            try:
                return partition.mountpoint
            except PermissionError:
                continue
def get_file_system_info():
    for partition in psutil.disk_partitions():
        if 'fixed' in partition.opts or 'rw' in partition.opts:
            try:
                return partition.fstype
            except PermissionError:
                continue
def get_capacity_info():
    for partition in psutil.disk_partitions():
        if 'fixed' in partition.opts or 'rw' in partition.opts:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                return (usage.total / (1024 ** 3))
            except PermissionError:
                continue
def get_usage_info():
    for partition in psutil.disk_partitions():
        if 'fixed' in partition.opts or 'rw' in partition.opts:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                return (usage.used / (1024 ** 3))
            except PermissionError:
                continue

# get_network_info
def get_interface_info():
    interface_info = []
    
    for interface, addrs in psutil.net_if_addrs().items():
        af_inet = [x for x in addrs if x.family == socket.AF_INET]
        for addr in af_inet:
            interface_info.append(interface)
    return interface_info        
def get_ipv4_info():
    ipv4_info = []
    
    for interface, addrs in psutil.net_if_addrs().items():
        af_inet = [x for x in addrs if x.family == socket.AF_INET]
        for addr in af_inet:
            ipv4_info.append(addr.address)
    return ipv4_info

# get_procesosr_info
def get_processor_manufacturer_info():
    return cpuinfo.get_cpu_info().get('vendor_id_raw','Unknown')
def get_processor_model_info():
    return cpuinfo.get_cpu_info().get('brand_raw','Unknown')

# get_gpu_info
def get_gpu_model_info():
    gpu_model = []
    
    try:
        gpus = GPUtil.getGPUs()
        
        if len(gpus) == 0:
            gpu_model.append(None)
        else:
            for i, gpu in enumerate(gpus):
                gpu_model.append(gpu.name)
    except Exception as e:
        print(f"Error occurred while getting graphics card info: {e}")
        
    return gpu_model
def get_gpu_total_memory_info():
    gpu_total_memory = []
    
    try:
        gpus = GPUtil.getGPUs()
        
        if len(gpus) == 0:
            gpu_total_memory.append(None)
        else:
            for i, gpu in enumerate(gpus):
                gpu_total_memory.append(gpu.memoryTotal)
    except Exception as e:
        print(f"Error occurred while getting graphics card info: {e}")
        
    return gpu_total_memory
def get_gpu_used_memory_info():
    gpu_used_memory = []
    
    try:
        gpus = GPUtil.getGPUs()
        
        if len(gpus) == 0:
            gpu_used_memory.append(None)
        else:
            for i, gpu in enumerate(gpus):
                gpu_used_memory.append(gpu.memoryUsed)
    except Exception as e:
        print(f"Error occurred while getting graphics card info: {e}")
        
    return gpu_used_memory
def get_gpu_free_memory_info():
    gpu_free_memory = []
    
    try:
        gpus = GPUtil.getGPUs()
        
        if len(gpus) == 0:
            gpu_free_memory.append(None)
        else:
            for i, gpu in enumerate(gpus):
                gpu_free_memory.append(gpu.memoryFree)
    except Exception as e:
        print(f"Error occurred while getting graphics card info: {e}")
        
    return gpu_free_memory
def get_gpu_usage_info():
    gpu_usage = []
    
    try:
        gpus = GPUtil.getGPUs()
        
        if len(gpus) == 0:
            gpu_usage.append(None)
        else:
            for i, gpu in enumerate(gpus):
                gpu_usage.append(gpu.load * 100)
    except Exception as e:
        print(f"Error occurred while getting graphics card info: {e}")
        
    return gpu_usage
def get_gpu_memory_usage_info():
    gpu_memory_usage = []
    
    try:
        gpus = GPUtil.getGPUs()
        
        if len(gpus) == 0:
            gpu_memory_usage.append(None)
        else:
            for i, gpu in enumerate(gpus):
                gpu_memory_usage.append((gpu.memoryUsed / gpu.memoryTotal) * 100)
    except Exception as e:
        print(f"Error occurred while getting graphics card info: {e}")
        
    return gpu_memory_usage

# show function
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
        gpus = GPUtil.getGPUs()
        if len(gpus) == 0:
            print('None GPU')
        else:
            for i, gpu in enumerate(gpus):
                print(f"------ GPU {i + 1} ------")
                print(f"Model: {gpu.name}")
                print(f"Total memory (MB): {gpu.memoryTotal}")
                print(f"Used memory (MB): {gpu.memoryUsed}")
                print(f"Free memory (MB): {gpu.memoryFree}")
                print(f"GPU usage (%): {gpu.load * 100}%")
                print(f"Memory usage (%): {(gpu.memoryUsed / gpu.memoryTotal) * 100}%")
    except Exception as e:
        print(f"Error occurred while getting graphics card info: {e}")
        

# All show Function
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
