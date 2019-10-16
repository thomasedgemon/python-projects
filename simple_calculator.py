import os
import sys

print("Type 1 for Addition")
print("Type 2 for Subtraction")
print("Type 3 for Multiplication")
print("Type 4 for Division")
print("Type 5 for Exponentiation")
while True:
    user_choice = int(input ("What operation would you like to perform?: "))

    if user_choice == 1:
        first_number = int(input ("What is the first number?: "))
        second_number = int(input ("What is the second number?: "))
        print( first_number + second_number , "is the answer")
    elif user_choice == 2:
        first_number = int(input ("What is the first number?: "))
        second_number = int(input ("What is the second number?: "))
        print( first_number - second_number , "is the answer")
    elif user_choice == 3:
        first_number = int(input ("What is the first number?: "))
        second_number = int( input ("What is the second number?: "))
        print( first_number*second_number , "is the answer")
    elif user_choice == 4:
        first_number = int( input ("what is the first number?: "))
        second_number = int(input ("What is the second number?: "))
        print( first_number/second_number , "is the answer")
    elif user_choice == 5:
        base = int( input ("what is the base?: "))
        exp = int( input ("What is the exponent?: "))
        print( base**exp , "is the answer" )
