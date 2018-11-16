#!/usr/bin/env python
import re

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"

print("It's a good idea")
print('Guido is "the man"!')

print("""Python is a 'great' language, and Guido is *still* "The Man\"""")

query = """
select * from customers
where lastname like "smith%"
"""


print(s1, s2)
print(s5)

conan = "What is best in life"
print(conan.find('i', 8, len(conan)))
print(conan.find('i', 8, None))

print([m.start() for m in re.finditer('i', conan)])
