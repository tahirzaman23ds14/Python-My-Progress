""" 
#############################################################################################
# What is a Variable?

A variable in Python is like a container (or a box) that stores information (data).
You can give this container a name and put a value inside it.
Later, you can reuse or change the value without rewriting everything.

👉 Think of it as giving a "label" to some data.

###############################################################################################################
# How Variables Work

You create a variable by assigning a value using the = sign.

Example:

x = 10     # variable 'x' stores the number 10
name = "Tahir"  # variable 'name' stores the text "Tahir"


Now, instead of writing the actual value again and again, you just use the variable name.

If the value changes, you only need to update the variable once."""
#############################################################################################################
# Practice with Variables
#Without variables (lots of repetition):
print("My name is Tahir")
print("Tahir is learning Python")
print("Tahir wants to become a Python Expert")


#👉 Problem: If you want to change the name, you must edit it everywhere.

#With variables (clean and easy):
# Assigning the name to a variable
name = "Ali"  

# Now use 'name' instead of repeating the text
print("My name is", name)
print(name, "is learning Python")
print(name, "wants to become a Python Expert")

#Updating Variable Values

#ariables can be updated anytime by assigning a new value:

name = "Ali"
print("My name is", name)

name = "Sara"  # changed value
print("Now my name is", name)

#Key Points About Variables in Python
"""
Naming Rules:

Start with a letter or _ (underscore).

Cannot start with a number.

Only letters, numbers, and _ are allowed.

Example: student_name, age, _id ✅
❌ Invalid: 1name, my-name

Case Sensitive:

Name and name are different variables.

Data Types (values stored in variables can be different types):
"""
age = 20          # integer
pi = 3.14         # float (decimal)
name = "Tahir"    # string (text)
is_student = True # boolean (True/False)


##### make more variable




#👉 Final Note: Variables make code reusable, readable, and easy to update.

