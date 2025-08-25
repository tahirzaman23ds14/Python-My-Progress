"""What input() does

 1 Waits for the user to type something and press Enter.

 2 Returns a string (type str).

 3 Removes the trailing newline that you typed when you hit Enter.

 4 Signature: input(prompt=None)
"""
name = input("Enter your name: ")   # prompt is optional
print(type(name))                   # <class 'str'>