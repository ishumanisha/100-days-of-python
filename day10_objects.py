# Day 10: Objects in Python

a = [1, 2, 3]
b = a

print("a =", a)
print("b =", b)

print("a == b:", a == b)
print("a is b:", a is b)

b.append(4)

print("After changing b:")
print("a =", a)
print("b =", b)