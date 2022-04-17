import math

def is_even(n):
    return n % 2 == 0


def is_prime(numero):
    count = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            count += 1
    return count == 2
            
        
def is_odd(n):
    return n % 2 != 0
