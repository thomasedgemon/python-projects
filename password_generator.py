
import random
import numpy as np

#dataset to pull from: 36 characters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#where the final password will be appended to one character at a time           
password = []

#user deciding how many digits they want in the password
desired_length = int(input("How many digits would you like your password to be?: "))
print("this will create a unique password out of")
print(36 ** desired_length)
print("possible outcomes!")

#if random generator returns 1, a random value is pulled from letters
#if random generator returns 0, a random value is pulled from the numbers
#each iterated character is appended to the password being built.

count = 0
while count < desired_length:
    random_integer = random.randint(0, 1)
    if random_integer == 0:
        password.append(np.random.choice(alphabet))
    else:
        password.append(np.random.choice(numbers)) 
    count += 1

#convert mixed array of int and str to all str iteratively
new_password = ''.join(str(x) for x in password) 

#deliver new password
print(f" your new password is {new_password}")

