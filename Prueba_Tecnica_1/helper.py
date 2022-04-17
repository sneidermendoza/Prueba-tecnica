import math

def is_even(n):
    return n %2 == 0


def is_prime(n):
    if n < 2:
        return False
    raiz = int(math.sqrt(n)) + 1
    for i in range(2, raiz):
        return n % i == 0
            
        
def is_odd(n):
    return n % 2 != 0
