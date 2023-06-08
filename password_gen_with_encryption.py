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

#this works. don't fuck with it. 

#master_password = input("what is the master password?: ")
#password_salt = "ca 0e 90 0b 44 7f bc ce 18 f6 42 b2 b9 1b e2 f2"
#plaintext = input("what is to be encrypted?: ")
#IV = Random.new().read(AES.block_size)
#key = pbkdf2.PBKDF2(master_password, password_salt).read(32)
#aes = pyaes.AESModeOfOperationCTR(key)
#ciphertext = aes.encrypt(plaintext)
#print(ciphertext)
#aes = pyaes.AESModeOfOperationCTR(key)
#decrypted = aes.decrypt(ciphertext)
#print(decrypted)

