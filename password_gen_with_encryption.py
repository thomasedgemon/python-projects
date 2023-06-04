import random
import numpy as np
import secrets
import cryptography
from cryptography.fernet import Fernet
import csv

def generate():
    #dataset to pull from: 36 characters
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    special_characters = ['@', '#', '*', '%', '$', '!']

    #where the final password will be appended to one character at a time           
    password = []
    first_choice = [0, 1, 2]
    #user deciding how many digits they want in the password
    desired_length = int(input("How many digits would you like your password to be?: "))
    print(f"this will create a unique password out of" + 42 ** desired_length + "outcomes")

    #if random generator returns 1, a random value is pulled from numbers
    #if random generator returns 0, a random value is pulled from the alphabet
    #if random generator returns 2, a random value is pulled from the special characters
    #each iterated character is appended to the password being built.

    count = 0
    while count < desired_length:
        random_integer = secrets.choice(first_choice)
    if random_integer == 0:
        password.append(secrets.choice(alphabet))
    elif random_integer == 1:
        password.append(secrets.choice(numbers)) 
    elif random_integer == 2:
        password.append(secrets.choice(special_characters))
        
    count += 1

    #convert mixed array of int and str to all str iteratively
    new_password = ''.join(str(x) for x in password) 

    #deliver new password
    print(f" your new password is {new_password}")

#encrypt passwords with AES256. symmetric key encryption via fernet
    #create key with fernet
#master_password = Fernet.generate_key() #how robust is fernet? look it up...
#master_password = str(master_password)
#print(f'your master password is' + master_password + 'do not share this with anyone')

#function for encrypting

def encrypt():
    #encrypt new password with master password via AES
    #save encrypted password to csv file with some kind of str designator to indicate what it's for
    #how are csv files organized??
    # OR save encryption here in a variable named after the designator???
        # how to differentiate stuff that's being encrypted as it's being encrypted?
    master_password = input("what is the master password?: ")
    password_to_encrypt = input("what is the password to be encrypted?: ")

def decrypt():
    #how to specify particular hash? based on its csv pair/designator?
    master_password = input("what is the master password?: ")
    password_to_decrypt = input("what is the password to be decrypted?: ")




user_input = str(input("what are we doing today? type 1 for password generation, 2 for password encryption, or 3 for password decryption: "))

if user_input == "1":
    generate()
elif user_input == "2":
    encrypt()
elif user_input == "3":
    decrypt()