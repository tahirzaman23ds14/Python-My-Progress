"""
#########################################################################################
 What is input() in Python?

The input() function is used to take input from the user.

It pauses the program, waits for the user to type something, and then returns that as text (string).
"""

########################################################################################
# Basic Example
name = input("Enter your name: ")
print("Hello,", name)


# When you run it:
""" 
Enter your name: Tahir
Hello, Tahir
"""

# #####################################################################################
# Important Point
""" 
input() always gives data in string (text) form.
Even if you type a number, it will still be a string.
"""
age = input("Enter your age: ")
print(age)         # if you type 20 → it prints 20
print(type(age))   # <class 'str'>


#######################################################################################
# How to use numbers from input
# If you want to use numbers (for calculation), you must convert them.

age = int(input("Enter your age: "))   # convert to integer
print("Next year your age will be", age + 1)

# If you type 20, it prints:
# Next year your age will be 21


#######################################################################################
""" 

Summary for Beginners

input() → always returns string

Use int() or float() if you need numbers

Put a message inside input("...") to guide the user

Small Practice for You:

Ask the user for their name and print a greeting.

Ask for two numbers and print their sum.

"""


############################################## Q U E S T I O N S ######################################################
""" 
 if we simply use input, why does the program not show anything? For example,
 when I give my name and hit Enter, nothing happens
"""
# ANSWER

# Case 1: Only writing input()
input()
""" 
What happens?

The program waits for you to type something.

After you press Enter, Python stores it — but you didn’t tell Python what to do with it.

That’s why it looks like “nothing happened.”
"""
#  Case 2: Storing the input in a variable
name = input()

""" 
Program still waits for you to type something.

After Enter, it saves what you typed in the variable name.

But still, nothing shows — because you didn’t tell Python to print it.

"""
# Case 3: Showing (printing) the input

name = input("Enter your name: ")
print("You typed:", name)
👉 Now it will:

Show a message asking for your name.

Wait for you to type and press Enter.

Print what you typed. ✅

🔑 Main Rule:
input() takes input

print() shows output

If you only write input() → program takes input but you see nothing, because no output is printed.

