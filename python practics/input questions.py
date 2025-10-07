# There are 10 Different question from Each using string , int , floating

"""
Question:1
Write a program that takes two integers from the user and prints their sum, difference, product, and quotient.
Answer """
number1= int(input("Enter Number :"))
number2= int(input("Enter Second number :"))

print(" Sum of two number is:", number1+number2 )
print("difference of two number is:",number1-number2 )
print("product of two number is:", number1 * number2)
print("quotient of two number is:", number1/number2)

""" 
Question:2
Take an integer from the user and print its square and cube.
Answer"""

numbers = int(input("Enter your number "))
print("here square is :", numbers ** 2 )
print("here cube is" , numbers ** 3)

""" 
Question:3
Take temperature in Celsius (float) and convert to Fahrenheit.
Answer """
celsius = int(input("Enter Celsuis Temperature to conver into "))
Fahrenheit = (celsius * 9/5 )+32
print(Fahrenheit)