# Day 9: None and Type Checking

name = "Isha"
age = 22
marks = None

print("Name:", name)
print("Age:", age)
print("Marks:", marks)

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of marks:", type(marks))

print("Is age an integer?", isinstance(age, int))
print("Is name a string?", isinstance(name, str))
print("Are marks missing?", marks is None)