#!/usr/bin/env python
import os

os.system("hostname")   # <1>

with os.popen('netstat -an') as netstat_in:  # <2>
    for entry in netstat_in:  # <3>
        if 'ESTABLISHED' in entry:   # <4>
            print(entry, end='')
print()

with os.popen("hostname") as hostname_in:
    hostname = hostname_in.read().rstrip()

print(hostname)
print("done")
