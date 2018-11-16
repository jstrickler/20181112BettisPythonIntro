#!/usr/bin/env python

import re


s = """lorem ipsum M302 dolor sit amet, consectetur r99 adipiscing elit, sed do
 eiusmod tempor incididunt H476 ut labore et dolore magna Q51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo z883  consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A110 cupidatat non proident, sunt in H332 culpa qui 
officia deserunt Y45 mollit anim id est laborum"""

x = "wombat"

pattern = r'[A-Z]\d{2,3}'  # <1>

if re.search(pattern, s):  # <2>
    print("Found pattern.")
else:
    print("NOT FOUND")
print()

#   m/RE/gmisx

# re.NONE  == 0
m = re.search(pattern, s, re.IGNORECASE | re.VERBOSE)  # <3>
print(m)
if m:
    print("Found:", m.group(0)) # <4>
    print("Found:", m.group())  # <4>
print()

for m in re.finditer(pattern, s): # <5>
    print(m.group())
print()

matches = re.findall(pattern, s)  # <6>
print("matches:",  matches)

match_list = list(re.finditer(pattern, s))
print(match_list)

matches = [m.group() for m in match_list]
