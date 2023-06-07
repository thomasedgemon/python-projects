import secrets
import csv
import base64
import cryptography
from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA256
from builtins import bytes
import hashlib
import Cryptodome
from Cryptodome import Random

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

master_password = input("what is the master password?: ")
password_to_encrypt = input("what password are we encrypting?: ")

#def encrypt(master_password, password_to_encrypt):
key = (pbkdf2.crypt(master_password)).encode() #is now bytes-class of length 48. needs to be 32 bytes.
#initialization vector
IV = Random.new().read(AES.block_size) #IV is now bytes-class
#hash master password
hashed_pass = SHA256.new(master_password.encode('utf-8')).digest() #is now bytes-type
encryptor = AES.new(key, AES.MODE_CBC, IV=IV)
print(type(encryptor))
#final_encrypted = encryptor.encrypt(password_to_encrypt)
#print(type(final_encrypted))

    





user_option = input("what are we doing today? type 1 to generate a new password, 2 to encrypt a password, or 3 to decrypt as password: ")
if user_option == "1":
    generate()
elif user_option == "2":
    master_password = input("what is the master password?: ")
    password_to_encrypt = input("what is the password to be encrypted?: ")
    password_to_key()
    make_initialization_vector()
    encrypt(password_to_encrypt, master_password)
    pad_string()
    encode()
    
elif user_option == "3":
    master_password = input("what is the master password?: ") 
    password_to_decrypt = input("what is the password to be decrypted?: ")
    password_to_key()
    make_initialization_vector()
    #pad_string()
    decode()
    unpad_string()
    decrypt()
