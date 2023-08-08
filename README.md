# Sys_info
It's a package that allows you to easily find out the system information of your computer through Python

> planning to switch to pip through Pypi in the future
# PiP install
```
pip install psutil py-cpuinfo pynvml
```
# import
```python
import platform
import psutil
import subprocess
import cpuinfo
import socket
from pynvml import nvmlInit, nvmlDeviceGetCount, nvmlDeviceGetHandleByIndex, nvmlDeviceGetName, nvmlDeviceGetMemoryInfo, nvmlDeviceGetUtilizationRates, nvmlShutdown
```
# ETC
> For improvements, please call Full Requests
> 
> Mail : gms8757@naver.com
