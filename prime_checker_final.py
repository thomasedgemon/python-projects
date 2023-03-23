

def is_prime(n):
    if n == 2 or n == 3:
        print("this number is prime")
    elif (n+1) % 6 == 0 or (n-1) % 6 == 0:
        print("this number is prime")
    else:
        print("this number is composite")
n = int(input("what number am i checking?: "))

is_prime(n)