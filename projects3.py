# ==========================================
# PART 1: Numbers, Strings and Booleans
# ==========================================

# 1. Integer & Float Mix
a = 10
b = 3.5

print("Addition:", a + b, type(a + b))
print("Subtraction:", a - b, type(a - b))
print("Multiplication:", a * b, type(a * b))
print("Division:", a / b, type(a / b))

# ==========================================

# 2. Large Integer & Type
large_num = 9876543210123456789
print("\nLarge Integer:", large_num)
print("Type:", type(large_num))

# ==========================================

# 3. Complex Number Basics
z = 3 + 4j
z2 = 1 + 2j

print("\nComplex Number:", z)
print("Real Part:", z.real)
print("Imaginary Part:", z.imag)
print("Type:", type(z))
print("Addition:", z + z2)

# ==========================================

# 4. Boolean from Comparisons
m = 10
n = 15

status = (m > n)
print("\nStatus:", status)
print("Type:", type(status))

status = (m != n)
print("Status:", status)

# ==========================================

# 5. String Creation & Indexing
text = "HelloWorld"

print("\nFirst Character:", text[0])
print("Last Character:", text[-1])
print("Length:", len(text))

# ==========================================

# 6. String Slicing
lang = "PythonProgramming"

print("\nIndex 2 to 8:", lang[2:9])
print("Start to Index 5:", lang[:6])
print("Reverse:", lang[::-1])

# ==========================================

# 7. String Methods
phrase = " Hello, Python World! "

print("\nOriginal:", phrase)
print("Strip:", phrase.strip())
print("Upper:", phrase.upper())
print("Replace:", phrase.replace("Python", "Java"))

# Strings are immutable.
# Methods return a new string.

# ==========================================

# 8. String Formatting
name = "Rajesh"
score = 95

print("\nUsing Concatenation:")
print(name + " scored " + str(score) + " points.")

print("Using f-string:")
print(f"{name} scored {score} points.")

# ==========================================

# 9. Boolean Operations
result = not(True and False) or (5 > 3)

print("\nBoolean Result:", result)

# True and False = False
# not False = True
# True or True = True

# ==========================================

# 10. List Creation & Access
numbers = [12, 25, 38, 44, 59]

print("\nFirst:", numbers[0])
print("Middle:", numbers[2])
print("Last:", numbers[-1])

# ==========================================

# 11. List Insertion & Deletion
nums = [10, 20, 30, 40]

nums.insert(2, 25)
nums.pop()

print("\nUpdated List:", nums)

# ==========================================

# 12. List Slicing
letters = ["a", "b", "c", "d", "e"]

print("\nSlice b,c,d:", letters[1:4])
print("Without first and last:", letters[1:-1])

# ==========================================

# 13. Sorting & Reversing
values = [8, 3, 10, 2, 6]

values.sort()
print("\nSorted:", values)

values.reverse()
print("Reversed:", values)

# ==========================================

# 14. Combining Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2
print("\nUsing + :", combined)

list3 = [1, 2, 3]
list3.extend(list2)
print("Using extend():", list3)

# ==========================================

# 15. Aggregating List Values
floats = [2.5, 3.6, 1.2, 5.0]

print("\nSum:", sum(floats))
print("Minimum:", min(floats))
print("Maximum:", max(floats))
# ==========================================
# PART 2: Tuples and Sets
# ==========================================

# 16. Tuple Creation
t = (10, 20, "Hello", True)

print("Tuple:", t)
print("Type:", type(t))

# ==========================================

# 17. Tuple Indexing & Slicing

print("\nFirst Two Elements:", t[:2])
print("Last Element:", t[-1])

# ==========================================

# 18. Tuple Unpacking

t2 = ("Tom", 25, "Engineer")

name, age, profession = t2

print("\nName:", name)
print("Age:", age)
print("Profession:", profession)

# ==========================================

# 19. Attempt Tuple Mutation

# Uncomment the line below to see the error.
# t[0] = 999

# Tuples are immutable.
# Their elements cannot be changed after creation.

# ==========================================

# 20. Set Creation & Membership

my_set = {1, 3, 5, 7}

print("\n5 in my_set:", 5 in my_set)
print("2 not in my_set:", 2 not in my_set)

# ==========================================

# 21. Add & Remove Elements

my_set.add(9)
my_set.remove(3)

print("\nUpdated Set:", my_set)

# ==========================================

# 22. Set Operations

setA = {1, 2, 3}
setB = {3, 4, 5}

print("\nUnion:", setA | setB)
print("Intersection:", setA & setB)
print("Difference (setA - setB):", setA - setB)

# ==========================================

# 23. Check Unique Values

vals = [1, 2, 2, 3, 3, 3, 4]

unique_vals = set(vals)

print("\nOriginal List:", vals)
print("Set:", unique_vals)

# Sets automatically remove duplicate values.

# ==========================================

# 24. Frozenset Creation

fs = frozenset([2, 4, 4, 6])

print("\nFrozenset:", fs)

# Duplicate values are removed.
# Frozensets are immutable.

# ==========================================

# 25. Tuple Concatenation & Replication

tuple1 = (1, 2)
tuple2 = (3, 4)

print("\nConcatenation:", tuple1 + tuple2)
print("Replication:", tuple1 * 3)

# ==========================================

# 26. Single-Element Tuple

a = (42,)
b = (42)

print("\na:", a, type(a))
print("b:", b, type(b))

# A trailing comma makes it a tuple.

# ==========================================

# 27. Intersection & Union

setA = {1, 2, 3, 4}
setB = {1, 2, 3}

print("\nIntersection:", setA & setB)
print("Union:", setA | setB)

# ==========================================

# 28. Subset and Superset

print("\nIs setB subset of setA?:", setB.issubset(setA))
print("Is setA superset of setB?:", setA.issuperset(setB))
# ==========================================
# PART 3: Operators and Built-in Functions
# ==========================================

# 29. Operator Precedence

a = 4
b = 2
c = 5

print("a + b * c =", a + b * c)
print("(a + b) * c =", (a + b) * c)

# Multiplication has higher precedence than addition.
# Parentheses force addition to happen first.

# ==========================================

# 30. Modulo & Floor Division

x = 17
y = 4

print("\nRemainder (x % y):", x % y)
print("Floor Division (x // y):", x // y)

# % returns the remainder.
# // returns the quotient without the decimal part.

# ==========================================

# 31. Power Operator

print("\n2 ** 3 =", 2 ** 3)

power = 3 ** 4
print("3 ** 4 =", power)

print("Addition =", (2 ** 3) + (3 ** 4))

# ==========================================

# 32. String Comparison

print("\n'apple' < 'banana':", "apple" < "banana")
print("'apple' > 'banana':", "apple" > "banana")
print("'apple' == 'banana':", "apple" == "banana")

# ==========================================

# 33. Mixed Type Comparison

print("\n5 == 5.0:", 5 == 5.0)
print("5 is 5.0:", 5 is 5.0)

# == compares values.
# is compares whether both objects are the same object in memory.

# ==========================================

# 34. Chain Comparisons

print("\n2 < 3 < 5:", 2 < 3 < 5)

# Python evaluates it as:
# (2 < 3) and (3 < 5)

# ==========================================

# 35. Logical AND

p = True
q = False

print("\np and q:", p and q)

age = 20
has_ID = True

print("Can Enter:", (age > 18) and (has_ID == True))

# ==========================================

# 36. Logical OR

print("\np or q:", p or q)

# ==========================================

# 37. Logical NOT

r = (10 > 5)

print("\nr:", r)
print("not r:", not r)

# ==========================================

# 38. Using len()

numbers = [1, 2, 3, 4, 5, 6, 7]

print("\nLength:", len(numbers))

# ==========================================

# 39. Using type()

print("\nType of 10:", type(10))
print("Type of 10.5:", type(10.5))
print("Type of 'ten':", type("ten"))
print("Type of True:", type(True))
print("Type of 3+2j:", type(3 + 2j))

# Data types:
# int
# float
# str
# bool
# complex

# ==========================================

# 40. Using abs()

print("\nabs(10):", abs(10))
print("abs(-10):", abs(-10))
print("abs(-3.5):", abs(-3.5))

# abs() returns the positive distance from zero.

# ==========================================

# 41. Using round()

print("\nround(3.14159,2):", round(3.14159, 2))
print("round(2.5):", round(2.5))

# Python uses "Banker's Rounding".
# round(2.5) becomes 2.

# ==========================================

# 42. Using sum(), max(), min()

values = [12, 5, 20, 8, 15]

print("\nSum:", sum(values))
print("Maximum:", max(values))
print("Minimum:", min(values))

# ==========================================

# 43. Using sorted()

vals = (3, 1, 4, 2)

print("\nSorted:", sorted(vals))
print("Original Tuple:", vals)

# sorted() returns a new list.
# The original tuple remains unchanged.

# ==========================================

# 44. Using any() and all()

bool_list = [True, False, True]

print("\nany():", any(bool_list))
print("all():", all(bool_list))

# any() returns True if at least one value is True.
# all() returns True only if every value is True.

# ==========================================

# 45. Storing Booleans from Comparisons

a = (10 > 3)
b = (5 == 5)

print("\na:", a)
print("b:", b)
print("a and b:", a and b)
print("a or b:", a or b)

# ==========================================

# 46. More Comparison Examples

print("\n15 >= 10:", 15 >= 10)
print("8 <= 5:", 8 <= 5)
print("9 != 9:", 9 != 9)

# ==========================================

# 47. Boolean Expression

result = (10 > 5) and (8 < 12) or False

print("\nBoolean Expression Result:", result)
# ==========================================
# PART 4: Advanced Strings & Final Tasks
# ==========================================

# 48. Multiline String & Counting

hobby = """
I like playing football.
I also enjoy reading books.
Football helps me stay active.
"""

count_a = hobby.lower().count("a")

print("Multiline String:")
print(hobby)
print("Count of 'a':", count_a)

# lower() makes the search case-insensitive.

# ==========================================

# 49. Advanced String Slicing

text = "ABCDEFGHIJ"

print("\nEvery Second Character:", text[::2])
print("Reverse:", text[::-1])

# ==========================================

# 50. Casefold vs Lower

s1 = "Case"
s2 = "case"

print("\nDirect Comparison:", s1 == s2)
print("After casefold():", s1.casefold() == s2.casefold())

# casefold() is stronger than lower() for
# case-insensitive comparisons in different languages.

# ==========================================

# 51. Formatted Printing

name = "Ramesh"
product = "Notebook"
quantity = 2
price = 12.50

print(f"\n{name} purchased {quantity} {product} for a total of ${quantity * price}")

# ==========================================

# 52. Type Conversion Chain

num = input("\nEnter a number: ")

float_num = float(num)
bool_num = bool(float_num)

print("Float:", float_num)
print("Boolean:", bool_num)

# Note:
# bool(0.0) -> False
# Any other number -> True

# ==========================================

# 53. String List Sorting

fruits = ["apple", "banana", "cherry"]

fruits.sort(reverse=True)
print("\nDescending:", fruits)

fruits.reverse()
print("After reverse():", fruits)

# ==========================================

# 54. Insert Using Slicing

nums = [2, 5, 7, 1, 9]

nums[1:1] = [4]

print("\nAfter Inserting 4:", nums)

# ==========================================

# 55. Indexing Within a Mixed List

info = ["John", 28, True, 4500.75]

print("\nName:", info[0])
print("Salary:", info[3])

# ==========================================

# 56. Tuple Concatenation & Replication

t1 = (1, 2)
t2 = (3, 4)

print("\nConcatenation:", t1 + t2)
print("Replication:", t1 * 3)

# ==========================================

# 57. Single-Element Tuple

a = (42,)
b = (42)

print("\na:", a, type(a))
print("b:", b, type(b))

# (42,) is a tuple.
# (42) is just an integer.

# ==========================================

# 58. Intersection & Union

setA = {1, 2, 3, 4}
setB = {1, 2, 3}

print("\nIntersection:", setA & setB)
print("Union:", setA | setB)

# ==========================================

# 59. Subset & Superset

print("\nSubset:", setB.issubset(setA))
print("Superset:", setA.issuperset(setB))

# ==========================================

# 60.

print("\nCongratulations!")
print("You have completed all the Python practice programs.")