'''
Escribe un programa que pida al usuario una cadena de texto y la imprima invertida.
'''

def reverse_text():
    text = input("Enter a string: ")  
    return text[::-1]

print(reverse_text())