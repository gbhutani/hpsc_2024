"""
$UWHPSC/codes/python/debugdemo1a.py

Debugging demo using print statements
"""

x = 3.
y = -22.

def f(z):
    x = z+10
    print(f"+++ in function f: x = {x}, y = {y}, z = {z}")
    return x

print(f"+++ before calling f: x = {x}, y = {y}")
y = f(x)
print(f"+++ after calling f: x = {x}, y = {y}")

