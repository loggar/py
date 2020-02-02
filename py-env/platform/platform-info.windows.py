#!/usr/bin/python3

import platform

# Architecture
print("Architecture: " + platform.architecture()[0])

# machine
print("Machine: " + platform.machine())

# node
print("Node: " + platform.node())

# system
print("System: " + platform.system())

# Windows
print("platform.win32_is_iot(): ", platform.win32_is_iot())
print("platform.win32_ver(): ", platform.win32_ver())

# processor
print("platform.processor()", platform.processor())
