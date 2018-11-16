#!/usr/bin/env python
"""
Parse Abaqus input file
"""

# What we want to do:
#
# Find first line with ELEMENT ...
# Replace it with predefined line
# Add some extra lines
#
# INPUTS: file name, predefined stuff
FILE_NAME = 'Fake.inp.txt'

replacement1 = """*USER ELEMENT, NODES=2, TYPE=U1, PROPERTIES=4, COORDINATES=3,
VARIABLES=12
1, 2, 3
"""
replacement2 = """*USER ELEMENT, NODES=5, TYPE=U1, PROPERTIES=4, COORDINATES=3,
VARIABLES=12
6, 5, 4
"""

TARGET1 = '*ELEMENT'
TARGET2 = '*ELEMENT'

with open(FILE_NAME) as file_in:
    with open(FILE_NAME + '.tmp', 'w') as file_out:
        for line in file_in:
            if line.startswith(TARGET1):
                file_out.write(replacement1)
                break
            else:
                file_out.write(line)

        for line in file_in:
            if line.startswith(TARGET2):
                file_out.write(replacement2)
                break
            else:
                file_out.write(line)

        file_out.write(file_in.read())
