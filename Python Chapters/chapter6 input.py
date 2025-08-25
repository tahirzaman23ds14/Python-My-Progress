"""
 What is input() in Python?

The input() function is used to take input from the user.

It pauses the program, waits for the user to type something, and then returns that as text (string).
"""

# ###########Basic Example
name = input("Enter your name: ")
print("Hello,", name)


# When you run it:
""" 
Enter your name: Tahir
Hello, Tahir
"""

# ##########Important Point
""" 
input() always gives data in string (text) form.
Even if you type a number, it will still be a string.
"""
age = input("Enter your age: ")
print(age)         # if you type 20 → it prints 20
print(type(age))   # <class 'str'>