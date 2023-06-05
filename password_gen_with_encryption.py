import numpy as np
import secrets
import csv
import base64
import cryptography
from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA256
from builtins import bytes
import random


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
    domain = str(42 ** desired_length)

    print(f"this will create a unique password out of " + domain + " outcomes")

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

def password_to_key(master_password):
    return SHA256.new(master_password).digest()

def make_initialization_vector():
    return random.new().read(AES.block_size)

def encrypt(password_to_encrypt, master_password):
    key = password_to_key(master_password)
    IV = make_initialization_vector()
    encryptor = AES.new(key, AES.MODE_CBC, IV)

def decrypt(password_to_decrypt, master_password):
    key = password_to_key(master_password)   
    IV = string[:AES.block_size]  
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    string = decryptor.decrypt(string[AES.block_size:])
    return unpad_string(string)

def pad_string(string, chunk_size=AES.block_size):
    assert chunk_size  <= 256, 'We are using one byte to represent padding'
    to_pad = (chunk_size - (len(string) + 1)) % chunk_size
    return bytes([to_pad]) + string + bytes([0] * to_pad)

def unpad_string(string):
    to_pad = string[0]
    return string[1:-to_pad]

def encode(string):
    return base64.b64encode(string).decode("latin-1")

def decode(string):
    return base64.b64decode(string.encode("latin-1"))

user_option = input("what are we doing today? type 1 to generate a new password, 2 to encrypt a password, or 3 to decrypt as password: ")
if user_option == "1":
    generate()
elif user_option == "2":
    master_password = input("what is the master password?: ")
    password_to_encrypt = input("what is the password to be encrypted?: ")
    password_to_key()
    make_initialization_vector()
    pad_string()
    encode()
    encrypt()
elif user_option == "3":
    master_password = input("what is the master password?: ") 
    password_to_decrypt = input("what is the password to be decrypted?: ")
    password_to_key()
    make_initialization_vector()
    pad_string()
    decode()
    unpad_string()
    decrypt()
