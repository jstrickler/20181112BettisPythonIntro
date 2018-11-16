#!/usr/bin/env python

def get_message():
    return "Hello, world"

m = get_message()

print(m)

print(get_message())
# print(get_message)
print()

def hello(whom="world"):
    print("Hello,", whom)

hello('world')
hello('Mom')
hello('Dolly')
hello()

def spam(p1, p2, p3, p4='default'):
    pass

spam(1,2,3,4)
spam(1,2,3)

def ham(p1, *others):
    print(p1)
    print(others, '\n')

ham('a')
ham('a', 'b', 'c')

things = ['d', 'e', 'f']
ham('foo', *things)



def toast(*, file_name, user_name="bob"):
    print(file_name, user_name, '\n')

toast(file_name='foo.txt', user_name='senor_idiot')
toast(file_name='bar.txt')

def config(**kv):
    for k, v in kv.items():
        print(k, v)

config(color='brown', city='Detroit', flower='marigold')

info = {'color': 'red', 'city': 'Reno', 'flower': 'rose'}

config(**info)




