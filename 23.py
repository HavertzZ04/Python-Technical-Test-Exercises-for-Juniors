'''
Escribe un programa que pida una lista de números al usuario y calcule la suma de los números pares y la suma de los números impares.
'''


def sum_even_odd(numbers_list):
    even_total = 0
    odd_total = 0
    
    for i in numbers_list:
        if i % 2 == 0:
            even_total += i
        else:
            odd_total += i
            
    return f"Even total: {even_total}\nOdd total: {odd_total}"

print(sum_even_odd([1,4,5,6,7,8,55,4,33,23,4,56,9]))
    