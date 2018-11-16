#!/usr/bin/env python
import sys

print(sys.version, '\n')
print(sys.version_info)
print(sys.version_info.major, '\n')

print(sys.prefix)
print(sys.executable, '\n')

for path in sys.path:
    print(path)
print()

print(sys.platform, '\n')

sys.stdout.write("HELLO\n")
print("LOOK OUT!!!!", file=sys.stderr)

