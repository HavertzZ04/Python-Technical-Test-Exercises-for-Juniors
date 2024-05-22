'''
Escribe un programa que implemente una cuenta regresiva desde un número especificado por el usuario.
'''

def countdown():
    n = int(input("Enter a number: "))
    
    for i in range(n, 0, -1):
        print(i)
    print("Boom!")
    
countdown()