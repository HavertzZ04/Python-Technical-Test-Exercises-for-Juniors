'''
Escribe un programa que genere una contraseña aleatoria de una longitud especificada por el usuario.
'''

from random import sample

def random_password():
    uppercase_letters = "ZXCVBNMASDFGHJKLQWERTYUIOP"
    lowercase_letters = "zxcvbnmasdfghjklqwertyuiop"
    digits = "1234567890"
    special_characters = "!@#$%^&*()-=_,./;'[]\<>?:}{|"
    
    characters = uppercase_letters + lowercase_letters + digits + special_characters
    
    lenght = int(input("Enter the password length: "))
    password = ''.join(sample(characters, lenght))
    
    return password

print(random_password())