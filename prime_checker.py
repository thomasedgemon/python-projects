
from math import isqrt
def is_prime(n):
    number = ""

    if n == 2 or n == 3:
        number = "P"
    elif (n+1) % 6 == 0 or (n-1) % 6 == 0:
        for i in range(4, isqrt(n)):
            if n % i == 0:
                number = "C"
            else:
                number = "P"
    else:
        number = "C"                   

    if number == "P":
        print("this number is prime")
    else:
        print("this number is composite")
        
n = int(input("what number am i checking?: "))


is_prime(n)