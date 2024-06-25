# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 23:21:20 2024

@author: ROBERT
"""

import platform

def gather_system_info():
    info = {
        "OS": platform.system(),
        "OS Release": platform.release(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Platform": platform.platform(),
        "Python Version": platform.python_version(),
        "Node Name": platform.node(),
        "Version Info": platform.version(),
        "Libc Info": platform.libc_ver()
    }
    return info

system_info = gather_system_info()
for key, value in system_info.items():
    print(f"{key}: {value}")
