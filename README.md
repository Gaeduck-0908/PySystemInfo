# PySystemInfo
- It's a package that allows you to easily find out the system information of your computer through Python
> PYPI : https://pypi.org/project/PySystemInfo/
# PiP install
```
pip install PySystemInfo
```
# Key Features
> [OS Information]
```python
platform.system() : OS
platform.version() : OS Version
platform.release() : OS Release
platform.machine() : OS Architecture
platform.processor() : Processor Name
```
> [CPU Information]
```python
psutil.cpu_count(logical=False) : CPU Core Count
psutil.cpu_count(logical=True) : CPU Thread Count
psutil.cpu_percent(interval=1) : CPU Usage
```
> [Memory Information]
```python
get_ram_info() : return count : 2
0 : Total_ram
1 : Available_ram
```
> [Disk Information]
```python
get_disk_info() : return count : 5
0 : Device
1 : Mount
2 : File System
3 : Capacity
4 : Usage
```
> [Network Information]
```python
get_network_info() : return count : 2
0 : Interface
1 : IPv4 Address
```
> [Motherboard Information]
```python
get_motherboard_info() : return count : 2
0 : Manufacturer
1 : Model
```
> [Processor Information]
```python
cpuinfo.get_cpu_info().get('vendor_id_raw') : Vendor ID
cpuinfo.get_cpu_info().get('hardware_raw') : Hardware
cpuinfo.get_cpu_info().get('brand_raw') : Brand
cpuinfo.get_cpu_info().get('hz_advertised_friendly') : Hz Advertised Friendly
cpuinfo.get_cpu_info().get('hz_actual_friendly') : Hz Actual Friendly
cpuinfo.get_cpu_info().get('hz_advertised') : Hz Advertised
cpuinfo.get_cpu_info().get('hz_actual') : Hz Actual
cpuinfo.get_cpu_info().get('arch') : Arch
cpuinfo.get_cpu_info().get('bits') : Bits
cpuinfo.get_cpu_info().get('count') : Count
cpuinfo.get_cpu_info().get('arch_string_raw') Arch String Raw
cpuinfo.get_cpu_info().get('l1_data_cache_size') : L1 Data Cache Size
cpuinfo.get_cpu_info().get('l1_instruction_cache_size') : L1 Instruction Cache Size
cpuinfo.get_cpu_info().get('l2_cache_size') : L2 Cache Size
cpuinfo.get_cpu_info().get('l2_cache_line_size') : L2 Cache Line Size
cpuinfo.get_cpu_info().get('l2_cache_associativity') : L2 Cache Associativity
cpuinfo.get_cpu_info().get('l3_cache_size') : L3 Cache Size
cpuinfo.get_cpu_info().get('stepping') : Stepping
cpuinfo.get_cpu_info().get('model') : Model
cpuinfo.get_cpu_info().get('family') : Family
cpuinfo.get_cpu_info().get('processor_type') : Processor Type
cpuinfo.get_cpu_info().get('flags') : Flags
```
> [Graphics Card Information]
```python
get_gpu_info : return : 6
0 : Model
1 : Total Memory
2 : Used Memory
3 : Free Memory
4 : GPU Usage
5 : Memory usage
```

# Example
```python
import PySystemInfo

print(PySystemInfo.print_system_info())
```
```python
import PySystemInfo

print(PySystemInfo.get_ram_info())
```
# ETC
> For improvements, please call Full Requests
> 
> Mail : gms8757@naver.com
