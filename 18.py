'''
Escribe un programa que encuentre todos los números perfectos entre 1 y 1000. Un número perfecto es un número que es igual a la suma de sus divisores propios positivos.
'''

def is_perfect(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number

def find_perfect_numbers(limit):
    perfect_numbers = []
    for num in range(1, limit + 1):
        if is_perfect(num):
            perfect_numbers.append(num)
    return perfect_numbers

perfect_numbers = find_perfect_numbers(1000)
print("Perfect numbers between 1 and 1000:", perfect_numbers)
