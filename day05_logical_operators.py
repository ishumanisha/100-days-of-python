# Day 5: Assignment and Logical Operators

age = 22
has_id = True

age += 1

print("Updated age:", age)
print("Eligible for entry:", age >= 18 and has_id)
print("Under 18 or has no ID:", age < 18 or not has_id)
print("Is age exactly 18?", age == 18)