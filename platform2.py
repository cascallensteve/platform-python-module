# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 23:25:10 2024

@author: ROBERT
"""

import platform

# Get the Python version
python_version = platform.python_version()
print(f"Python Version: {python_version}")

# Get the system's node (hostname)
node_name = platform.node()
print(f"Node Name: {node_name}")

# Get detailed version information
version_info = platform.version()
print(f"Version Info: {version_info}")

# Get information about the underlying libc library
libc_info = platform.libc_ver()
print(f"Libc Info: {libc_info}")
