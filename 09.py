'''
Escribe un programa que imprima los números del 1 al 50. Pero para los múltiplos de 3, imprime "Fizz" en lugar del número, y para los múltiplos de 5, imprime "Buzz". Para números que son múltiplos de ambos, imprime "FizzBuzz".
'''

def fizz_buzz():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz()
