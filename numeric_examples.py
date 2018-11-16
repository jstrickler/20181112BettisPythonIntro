#!/usr/bin/env python



i1 = 100
i2 = 0x100
i3 = 0b100
i4 = 0o100

print(i1, i2, i3, i4)

c1 = 1234j

print(c1)
print(type(c1))
print(c1.imag, c1.real)

f1 = 123.456
f2 = 123.
f3 = .456

bigint = 2930293825098230598230598203598203598203958209358203958209358209358203985209385029385029385029385029835092830598203958203985023850253

print(bigint + 1)


x = 23
y = 9

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x ** y)
print(x % y)
print(divmod(x, y))

x = 10
x += 5  # x = x + 5
x /= 3  # etc.
x *= 10
print(x)

# x = 5
# y = x++   # too crazy for Guido
# z = ++x
# print(x, y, z)


print(++x)
print(+++++++++++++++++++++++++++x)
print(-x)
print(--x)
print(-(-(-x)))

#  PEMDAS

# print((x + y) - (a * b))

x = 5
xx = float(x)
print(x, xx)

s1 = "  123.456   "
print(float(s1))

i1 = '1234'
print(int(i1) * 5)
print(i1 * 5)

thing = 'DeadBeef'
print("{:,d}".format(int(thing, 16)))



