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