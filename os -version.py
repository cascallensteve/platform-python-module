# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 23:22:54 2024

@author: ROBERT
"""

import platform

# Check if the system is running Windows
if platform.system() == "Windows":
    print("This system is running Windows.")

# Check if the system is running Linux
elif platform.system() == "Linux":
    print("This system is running Linux.")

# Check if the system is running macOS
elif platform.system() == "Darwin":
    print("This system is running macOS.")

# Handle other operating systems
else:
    print("This system is running an unknown operating system.")
