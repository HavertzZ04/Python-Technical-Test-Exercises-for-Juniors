'''
Escribe un programa que invierta los dígitos de un número entero introducido por el usuario.
'''

def reverse_numbers():
    number = input("Enter a number: ")
    return number[::-1]

print(reverse_numbers())