'''
Escribe un programa que pida al usuario su nombre y luego imprima un saludo personalizado.
'''

from random import choice

def greeting():
    name = input("Enter your name: ")

    greetings = [
        f"Good morning {name}", 
        f"Hi, {name}", 
        f"Welcome {name}"
    ]
    return choice(greetings)

print(greeting())