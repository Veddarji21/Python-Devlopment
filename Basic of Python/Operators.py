
#  Arithmetic Operators

print("=== Arithmetic Operators ===")
a = 10
b = 3
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)   # Floor Division
print("a % b =", a % b)     # Modulus
print("a ** b =", a ** b)   # Exponentiation

#  Assignment Operators

print("\n=== Assignment Operators ===")
x = 5
print("x =", x)
x += 3
print("x += 3 →", x)
x -= 2
print("x -= 2 →", x)
x *= 2
print("x *= 2 →", x)
x /= 3
print("x /= 3 →", x)
x %= 2
print("x %= 2 →", x)
x = 4
x **= 2
print("x **= 2 →", x)
x //= 3
print("x //= 3 →", x)

#  Comparison Operators

print("\n=== Comparison Operators ===")
a = 7
b = 5
print("a == b →", a == b)
print("a != b →", a != b)
print("a > b →", a > b)
print("a < b →", a < b)
print("a >= b →", a >= b)
print("a <= b →", a <= b)

#  Logical Operators

print("\n=== Logical Operators ===")
x = True
y = False
print("x and y →", x and y)
print("x or y →", x or y)
print("not x →", not x)

#  Identity Operators

print("\n=== Identity Operators ===")
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a is b →", a is b)
print("a is c →", a is c)
print("a is not c →", a is not c)

#  Membership Operators

print("\n=== Membership Operators ===")
fruits = ["apple", "banana", "cherry"]
print("'apple' in fruits →", "apple" in fruits)
print("'mango' not in fruits →", "mango" not in fruits)

#  Bitwise Operators

print("\n=== Bitwise Operators ===")
a = 5   # 0 1 0 1
b = 3   # 0 0 1 1
print("a & b →", a & b)  # Bitwise AND
print("a | b →", a | b)  # Bitwise OR
print("a ^ b →", a ^ b)  # Bitwise XOR
print("~a →", ~a)        # Bitwise NOT
print("a << 1 →", a << 1)  # Left Shift
print("a >> 1 →", a >> 1)  # Right Shift
