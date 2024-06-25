# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 23:25:41 2024

@author: ROBERT
"""

import platform

# Get the system's OS name
os_name = platform.system()
print(f"Operating System: {os_name}")

# Get the release version of the OS
os_release = platform.release()
print(f"OS Release: {os_release}")

# Get the machine type
machine_type = platform.machine()
print(f"Machine Type: {machine_type}")

# Get the processor type
processor_type = platform.processor()
print(f"Processor Type: {processor_type}")

# Get the full platform information
platform_info = platform.platform()
print(f"Platform Info: {platform_info}")
