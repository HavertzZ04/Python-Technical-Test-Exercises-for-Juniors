'''
Escribe un programa que imprima la tabla de multiplicar de un número introducido por el usuario.
'''

def multiplcate_table():
    number = int(input("Enter a number: "))
    
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
        
        
multiplcate_table()