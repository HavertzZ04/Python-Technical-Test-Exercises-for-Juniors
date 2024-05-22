'''
Escribe un programa que determine si un número de tres dígitos es un número Armstrong. Un número Armstrong es un número que es igual a la suma de los cubos de sus dígitos.
'''


def armstrong_number():
    number = input("Enter a number: ")
    number_split = [int(n) for n in number]
    total = 0
    
    for i in number_split:
        total += i ** len(number_split)
        
    if total == int(number):
        return f"{number} is an Armstrong Number"
    else:
        return f"{number} is not an Armstrong Number"
    
print(armstrong_number())