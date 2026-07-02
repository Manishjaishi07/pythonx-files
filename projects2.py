# ==========================================
# Python Data Structures Assignment
# Section 1: Lists
# ==========================================

# 1. Create a List
numbers = list(range(1, 16))
print("1. List:", numbers)

# 2. List of Strings
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("\n2. Favorite Fruits:", fruits)

# 3. Accessing Elements
lst = [10, 20, 30, 40, 50]
print("\n3. First Element:", lst[0])
print("Last Element:", lst[-1])

# 4. List Length
items = ["Book", "Pen", "Laptop", "Bottle", "Bag"]
print("\n4. Length of List:", len(items))

# 5. Appending Elements
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
print("\n5. Appended List:", numbers)

# 6. Inserting an Element
lst = [1, 3, 4]
lst.insert(1, 2)
print("\n6. After Inserting:", lst)

# 7. Removing an Element
lst = [1, 2, 3, 4, 5]
lst.remove(3)
print("\n7. After Removing 3:", lst)

# 8. Popping an Element
lst = [10, 20, 30, 40]
removed = lst.pop()
print("\n8. Popped Element:", removed)
print("Updated List:", lst)

# 9. Slicing a List
lst = [0, 1, 2, 3, 4, 5]
print("\n9. Slice (Index 2 to 4):", lst[2:5])

# 10. List Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print("\n10. Concatenated List:", result)

# 11. Repeating a List
lst = [1, 2]
print("\n11. Repeated List:", lst * 3)

# 12. Copying a List
original = [10, 20, 30]
copy_list = original.copy()
print("\n12. Original List:", original)
print("Copied List:", copy_list)

# 13. Clearing a List
lst = [1, 2, 3, 4]
lst.clear()
print("\n13. Cleared List:", lst)

# ==========================================
# Section 2: Tuples
# ==========================================

# 14. Create a Tuple
t = (1, 2, 3)
print("\n14. Tuple:", t)

# 15. Tuple of Strings
colors = ("Red", "Green", "Blue")
print("\n15. Colors Tuple:", colors)

# 16. Accessing Tuple Elements
t = (10, 20, 30, 40)
print("\n16. Second Element:", t[1])

# 17. Tuple Slicing
t = (0, 1, 2, 3, 4)
print("\n17. Slice (Index 1 to 3):", t[1:4])

# 18. Concatenating Tuples
t1 = (1, 2)
t2 = (3, 4)
print("\n18. Concatenated Tuple:", t1 + t2)

# 19. Tuple Unpacking
person = ("Alice", 25, "New York")
name, age, city = person
print("\n19. Name:", name)
print("Age:", age)
print("City:", city)

# 20. Convert List to Tuple
lst = [1, 2, 3, 4]
t = tuple(lst)
print("\n20. Converted Tuple:", t)

# 21. Counting Occurrences
t = (1, 2, 2, 3, 2)
print("\n21. Count of 2:", t.count(2))

# 22. Finding an Index
t = (10, 20, 30, 40)
print("\n22. Index of 30:", t.index(30))