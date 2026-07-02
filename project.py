# ==========================================
# 1. Basic Arithmetic and Type Identification
# ==========================================

integer_num = 10
float_num = 5.5
complex_num = 3 + 4j

print("Integer:", integer_num, "Type:", type(integer_num))
print("Float:", float_num, "Type:", type(float_num))
print("Complex:", complex_num, "Type:", type(complex_num))

# ==========================================
# 2. Arithmetic with Mixed Types
# ==========================================

a = 10
b = 3.5

print("\nSum:", a + b, "Type:", type(a + b))
print("Difference:", a - b, "Type:", type(a - b))
print("Product:", a * b, "Type:", type(a * b))
print("Quotient:", a / b, "Type:", type(a / b))

# ==========================================
# 3. Comparison Operators
# ==========================================

x = 10
y = 7

print("\nx > y:", x > y)    # True because 10 is greater than 7
print("x < y:", x < y)      # False because 10 is not less than 7
print("x == y:", x == y)    # False because 10 is not equal to 7
print("x != y:", x != y)    # True because 10 and 7 are different

# ==========================================
# 4. Boolean Variables
# ==========================================

status = True
print("\nStatus:", status)
print("Type:", type(status))

status = False
print("Status:", status)
print("Type:", type(status))

# ==========================================
# 5. String Creation and Length
# ==========================================

text = "Hello World"

print("\nString:", text)
print("Length:", len(text))
print("Type:", type(text))

# ==========================================
# 6. String Indexing
# ==========================================

s = "Python"

print("\nCharacters:")
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])

print("First Character:", s[0])
print("Last Character:", s[-1])

# ==========================================
# 7. String Slicing
# ==========================================

lang = "Programming"

print("\nSlice (0:5):", lang[0:5])
print("Slice (3:end):", lang[3:])
print("Without first 2 and last 2:", lang[2:-2])

# ==========================================
# 8. Exploring len() on Slices
# ==========================================

part1 = lang[:7]   # "Program"

print("\nPart1:", part1)
print("Length of part1:", len(part1))
print("Length of lang:", len(lang))
# part1 is shorter because it contains only part of the original string.

# ==========================================
# 9. String Methods – Case Conversion
# ==========================================

phrase = "Hello, Python!"

print("\nUpper:", phrase.upper())
print("Lower:", phrase.lower())
print("Original:", phrase)
# Original string remains unchanged because strings are immutable.

# ==========================================
# 10. Combining Strings
# ==========================================

str1 = "Data"
str2 = "Science"

combined = str1 + " " + str2

print("\nCombined String:", combined)
print("Length:", len(combined))

# ==========================================
# 11. In-Place vs. Reassignment
# ==========================================

word = "example"

word.upper()
print("\nWithout storing:", word)

word = word.upper()
print("After reassignment:", word)

# Strings are immutable.
# upper() returns a new string. The original string changes
# only when the returned value is assigned back.

# ==========================================
# 12. Arithmetic Operator Precedence
# ==========================================

a = 5
b = 3
c = 2

print("\na + b * c =", a + b * c)
print("(a + b) * c =", (a + b) * c)

# Multiplication has higher precedence than addition.
# Parentheses force addition to happen first.


# 13. String Index Out of Range

text = "Hello"

# Uncomment the following line to see the IndexError.
# print(text[10])

# IndexError occurs because index 10 does not exist in "Hello".
# Valid indexes are 0 to 4.


# 14. Equality vs. Identity Check

s1 = "test"
s2 = "test"

print("\ns1 == s2:", s1 == s2)
print("s1 is s2:", s1 is s2)

# == checks whether values are equal.
# is checks whether both variables refer to the same object in memory.

# ==========================================
# 15. Creating and Checking a Complex Number
# ==========================================

z = 3 + 4j

print("\nComplex Number:", z)
print("Real Part:", z.real)
print("Imaginary Part:", z.imag)
print("Type:", type(z))

# ==========================================
# 16. Comparisons with Floats
# ==========================================

f1 = 0.1 + 0.2
f2 = 0.3

print("\nf1 == f2:", f1 == f2)
print("f1:", f1)
print("f2:", f2)

# Floating-point numbers are stored approximately in binary,
# so 0.1 + 0.2 is not exactly equal to 0.3.