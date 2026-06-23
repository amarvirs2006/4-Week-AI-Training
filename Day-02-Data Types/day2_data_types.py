# Day 2: Python Collections

# ------------------ Lists ------------------

fruits = ["apple", "banana", "orange"]

# append()
fruits.append("mango")

# insert()
fruits.insert(1, "grapes")

# remove()
fruits.remove("banana")

# pop()
fruits.pop()

# count()
numbers = [1, 2, 2, 3, 2]
print("Count of 2:", numbers.count(2))

# index()
print("Index of orange:", fruits.index("orange"))

# copy()
fruits_copy = fruits.copy()

print("Fruits:", fruits)
print("Copied Fruits:", fruits_copy)


# ------------------ Tuples ------------------

colors = ("red", "blue", "green", "blue")

# count()
print("Count of blue:", colors.count("blue"))

# index()
print("Index of green:", colors.index("green"))


# ---------------- Dictionaries ----------------

student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

# get()
print("Name:", student.get("name"))

# keys()
print("Keys:", student.keys())

# values()
print("Values:", student.values())

# items()
print("Items:", student.items())

# update()
student.update({"city": "Delhi"})

# pop()
student.pop("age")

# copy()
student_copy = student.copy()

print("Student:", student)
print("Copied Dictionary:", student_copy)


# ------------------ Sets ------------------

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# add()
set1.add(7)

# remove()
set1.remove(2)

# discard()
set1.discard(10)     # No error if element doesn't exist

# pop()
removed_item = set1.pop()
print("Popped Item:", removed_item)

# copy()
set_copy = set1.copy()

# update()
set1.update({8, 9})

# union()
print("Union:", set1.union(set2))

# intersection()
print("Intersection:", set1.intersection(set2))

# difference()
print("Difference:", set1.difference(set2))

# issubset()
print({3, 4}.issubset(set2))

# issuperset()
print(set2.issuperset({3, 4}))

print("Set 1:", set1)
print("Copied Set:", set_copy)