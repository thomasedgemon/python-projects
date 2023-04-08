from math import isqrt
def is_prime(n):
    number = True

    if n == 2 or n == 3:
        number = True
    elif (n+1) % 6 == 0 or (n-1) % 6 == 0:
        for i in range(4, isqrt(n)):
            if n % i == 0:
                number = False
            else:
                number = True
    else:
        number = False                   

    if number is True:
        print("this number is prime")
    else:
        print("this number is composite")
        
n = int(input("what number am i checking?: "))


is_prime(n)