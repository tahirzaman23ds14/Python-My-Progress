############################################## What iS Data Types?

"""
In Python, a data type defines the kind of data a variable can store.
It tells Python whether the value is a number, text, True/False, or a collection.
"""


############################################  DATA TYPE BEHIND THE SEENS

"""
Behind the scenes, Python stores every value as an object, and each object has a specific data type (class).
This type information tells Python how much memory to use, how to represent the value, and what operations are allowed on it.

""" 

############################################## WHY PYTHON NEEDS DATA TYPES?

"""
Python needs data types to:

Identify the kind of data (number, text, True/False, etc.).

Decide memory size required to store the value.

Define valid operations (you can add numbers but not number + text).

Ensure correctness in calculations and logic.

👉 Without data types, Python wouldn’t know how to handle values properly. 

"""

############################################  DATA TYPES CATEGORIES
"""
In Python, data types are divided into categories:

Numeric Types → int, float, complex

Text Type → str

Boolean Type → bool

Sequence Types → list, tuple, range

Set Types → set, frozenset

Mapping Type → dict

None Type → NoneType


"""
################################## PRACTICE THE DATA TYPES

# Numeric
a = 10        # int
b = 3.14      # float
c = 2 + 3j    # complex

# Text
d = "Hello"   # str

# Boolean
e = True      # bool

# Sequence
f = [1, 2, 3]          # list
g = (4, 5, 6)          # tuple
h = range(5)           # range

# Set
i = {1, 2, 3}          # set
j = frozenset({4, 5})  # frozenset

# Mapping
k = {"name": "Tahir", "age": 20}  # dict

# None
l = None               # NoneType

# Checking data types
print(type(a))
print(type(b))
print(type(d))
print(type(e))
print(type(f))
print(type(k))
print(type(l))


