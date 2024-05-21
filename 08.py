'''
Escribe un programa que pida al usuario un número entero y calcule la suma de sus dígitos.
'''

def digits_sum():
    number = input("Enter a number: ")
    number_list = [int(num) for num in number]
    return sum(number_list)
    
print(digits_sum())