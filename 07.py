'''
Escribe un programa que imprima todos los números primos entre 1 y 100.
'''
from math import sqrt


def is_prime(number):    
    if number < 1:
        return False
    
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def prime_list():
    primes = []
    for i in range(1, 101):
        if is_prime(i):
            primes.append(i)
    return primes


print(prime_list())