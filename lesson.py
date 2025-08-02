"""
This script is a first attempt at data preprocessing and visualization
for practice in data science using Python.
"""

print("Shiawase")  # Get Started
 # Comment
"""
Just for comment
"""
create despair in the future
watch monster anime

z = 9  # Created variables
w = "Faris"
print(z)
print(w)
g = float("3.43")  # Casting
print(g)
h = "3.12"  # Type
print(type(h))

pyvar = "Shiawase"  # Able Variable's Names
py_var = "Shiawase"
_py_var = "Shiawase"
pyvaryVar = "Shiawase"
PYVAR = "Shiawase"
pyvar2 = "Shiawase"
# 2pyvar = "Shiawase"  # Unable Variable's Names
# py-var = "Shiawase"
# py var = "Shiawase"
pyVarVer = "Shiawase"  # Multi Words Variable Names, Camel Case
PyVarVEr = "Shiawase"  # Pascal Case
py_var_ver = "Shiawase"  # Snake Case

A, B, C = "Banana", "Apple", "Orange"  # Many Values to Multiple Variables
print(A, B, C)
a = b = c = "Arise"  # One Value to Multiple Variables
print(a, b, c)
Things = ["Ball", "Gloves", "Stick", "Field"]  # Unpacking
ab, bc, cd, de = Things
print(ab, bc, cd, de)

W = "Breathtaking"  # Global Variables


def myfunc():
    print("Python is so", W)


myfunc()

V = "Breathtaking"  # It's occuring when you create same variables but in different value and location


def myfunc():
    V = "Bored"
    print("Python is so", V)


myfunc()

print("Python is so", V)


def myfunc():  # Global Keyword
    global U
    U = "Awesome"


myfunc()

print("Python is so", U)

U = "Awesome"  # Global Keyword if you want change global variables inside function


def myfunc():
    global U
    U = "Fantastic"


myfunc()

print("Python is so", U)

V = dict(Name="John", Age=54)  # Data Types
print(V)
T = bool(6)
print(T)
S = bytes(4)
print(S)
R = bytearray(4)
print(R)
Q = memoryview(bytes(4))
print(Q)

P = 145  # Numeric Type Conversion
O = 26.765
N = 5
p = int(O)
o = float(P)
n = complex(N)

print(p), print(type(p))
print(o), print(type(o))
print(n), print(type(n))

(m, l, k) = (int(23), int("56"), int(5.6))  # Integer
print(m, l, k)
M, L, K = float(76), float(7.8), float("6.5")  # Float
print(M, L, K)
ml, lk, km = str("43"), str(56), str(67.7)  # String
print(ml, lk, km)

print(
    "I like you, 'Honey'"
)  # Qoutes Inside Quotes (You can use quotes inside a string, as long as they don't match the quotes surrounding the string)
W = "Breathtaking"  # Assign String to a Variable
W = """Breathtaking"""  # Multiline Strings
print(W[3])  # Strings are arrays
for W in "Breathtaking":  # Looping Through a String
    print(W)
W = "Breathtaking"  # Strings Length
print(len(W))
text = "I love for thousand, years"  # Check Strings
print("years" in text)
print("Gambit" in text)
text = "I love for thousand, years"  # Check Strings with If
if "love" in text:
    print("Yes, i don't fucking care.")
text = "I love for thousand, years"  # Check If Not Strings
print("years" not in text)
print("Gambit" not in text)
text = "I love for thousand, years"  # Check If Not Strings with If
if "Focus" not in text:
    print("Yes, i need fucking focus.")

text = "I love for thousand, years"  # Upper Case
print(text.upper())
print(text.lower())  # Lower Case
text = " I love for thousand, years "  # Remove Whitespaces
print(text.strip())
text = "I love for thousand, years"  # Replace Strings
print(text.replace("love", "Hate"))
text = "I, love for, thousand, years"  # Split Strings
print(text.split(","))

text = "I love for you thousand years,"  # Concatenation
txt = "Do i?"
print(text + " " + txt)
print(text, txt)

years = 2000  # F-Strings Format.
xtx = f"for you, {years} years ago"
print(xtx)


def factorial(n):  # Placeholder Practise
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def years(gs, sg, Sg):
    return factorial(gs) * sg * Sg


xtx = f"for you, {int(years(5, 10, 5/3))} years ago"
print(xtx)

print('I like you, "Honey"')  # Escape Character, Double Quotes
print("It's me")  # Single Quote
print("This will insert one \\ (backslash).")  # Backslash
print("It's\nme")  # New Line
print("I love \rfor you thousand years")  # Carriage Return
print("It's\tlike a child")  # Tab
print("Ett \bo....")  # Backspace
print("First part of text\fSecond part of text")  # Form Feed
txt = "\110\145\154\154\157"  # Octal Value \aaa
print(txt)
txt = "\x48\x65\x6c\x6c\x6f"  # Hex Value \xaa
print(txt)

#  String Methods
text = "       I love for thousand, years"  # Lstrip
print(text.lstrip())
text = "I love for thousand, years     "  # Rstrip
print(text.rstrip())
text = "I love for thousand, years"  # Startwith
print(text.startswith("for", 7, 9))
print(text.endswith("years", -6))  # Endwith
text = "I love for thousand, years"
print(text.find("for", 5, 11))  # Find (-1, if value not found)
print(text.index("for", 3, 16))  # Index (give an error, if value not found)
num = "34.536467"  # Isnumeric
print(num.isnumeric())
# There are isdigit, isalpha, isdecimal, and others
print(", ".join(Things))  # Join
text = "i love for thousand, years"
print(text.title())  # Title (Each first letter of words are capital)
print(text.capitalize())  # Capitalize (First letter of word is capital)

# This is a captain speaking right now.



