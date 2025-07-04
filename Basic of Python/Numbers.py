
#  Integer (int)
a = 10
print("Integer (int):", a, "| Type:", type(a))

#  Float (decimal number)
b = 10.5
print("Float (float):", b, "| Type:", type(b))

#  Complex number
c = 2 + 3j
print("Complex (complex):", c, "| Type:", type(c))

#  Arithmetic Operations
x = 7
y = 3

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)

#  Type Conversions
i = 5           # int
f = float(i)    # Convert to float
print("Convert int to float:", f)

f2 = 3.8
i2 = int(f2)    # Convert float to int
print("Convert float to int:", i2)

# Complex number from real & imaginary
real = 4
imag = 5
comp = complex(real, imag)
print("Complex from parts:", comp)

#  Absolute value
n = -12
print("Absolute value:", abs(n))

#  Round a float
num = 3.14159
print("Rounded number (2 decimals):", round(num, 2))

# Power & square root
print("5 to the power 3:", pow(5, 3))

import math
print("Square root of 25:", math.sqrt(25))


print("\n#️⃣ Summary of Types")
print("Type of a:", type(a))       # int
print("Type of b:", type(b))       # float
print("Type of c:", type(c))       # complex
