
#  String Declaration

print("=== String Declaration ===")
a = "Hello"
b = 'World'
c = """This is a 
multiline string."""
print(a)
print(b)
print(c)

#  Accessing Characters

print("\n=== Accessing Characters ===")
text = "Python"
print("First character:", text[0])
print("Last character:", text[-1])
print("Slice (1:4):", text[1:4])
print("Reverse:", text[::-1])

#  String Length

print("\n=== String Length ===")
print("Length of 'Python':", len(text))

#  String Concatenation

print("\n=== String Concatenation ===")
x = "Ved"
y = "Darji"
full_name = x + " " + y
print("Full Name:", full_name)

#  String Formatting

print("\n=== String Formatting ===")
age = 21
intro = f"My name is {x} and I am {age} years old."
print(intro)

#  Escape Characters

print("\n=== Escape Characters ===")
print("She said \"Hello!\"")
print("Line1\nLine2")
print("Tabbed\tText")

#  Common String Methods

print("\n=== String Methods ===")
s = "  python Programming  "

print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Title Case:", s.title())
print("Capitalize:", s.capitalize())
print("Strip spaces:", s.strip())
print("Replace:", s.replace("python", "Java"))
print("Split:", s.split())
print("Count 'm':", s.count('m'))
print("Find 'Program':", s.find('Program'))

#  String Comparison

print("\n=== String Comparison ===")
a = "apple"
b = "banana"
print("a == b:", a == b)
print("a != b:", a != b)
print("a < b:", a < b)  # Alphabetical order

#  String Membership

print("\n=== String Membership ===")
sentence = "Learning Python is fun"
print("'Python' in sentence:", "Python" in sentence)
print("'java' not in sentence:", "java" not in sentence)

# Useful Checks

print("\n=== Useful Checks ===")
test = "12345"
alpha = "abcDEF"
alphanum = "abc123"
space = "   "
print("test.isdigit():", test.isdigit())
print("alpha.isalpha():", alpha.isalpha())
print("alphanum.isalnum():", alphanum.isalnum())
print("space.isspace():", space.isspace())
print("'Hello'.startswith('H'):", "Hello".startswith("H"))
print("'Hello'.endswith('o'):", "Hello".endswith("o"))

#  Join Strings

print("\n=== Join Strings ===")
words = ["Python", "is", "awesome"]
joined = " ".join(words)
print("Joined sentence:", joined)
