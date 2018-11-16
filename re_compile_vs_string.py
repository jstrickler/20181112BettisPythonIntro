#!/usr/bin/env python
import re

pattern = r"[a-z]+"

s = """This is 10 times
the 2 dogs belonging to Bob have barked"""


s = ("This is 10 times "
"the 2 dogs belonging to Bob have barked"
)

found = re.findall(pattern, s)
print(found, '\n')

wombat = re.compile(pattern, re.I)

found = wombat.findall(s)
print(found)
