'''
Escribe un programa que genere un número aleatorio entre 1 y 100 y permita al usuario adivinarlo.
'''

from random import randint

def adivinate_number():
    random_number = randint(1, 100)
    tries = 10
    
    print("\nFind the number from 1 to 100")
    while True:
        print(f"Your tries are: {tries}")
        user_number = int(input("Enter a number: "))
        
        if user_number == random_number:
            print("You won")
            break
        elif user_number > random_number:
            print(f"{user_number} is greater than the secret number\n")
        elif user_number < random_number:
            print(f"{user_number} is less than the secret number\n")
            
        if tries == 1:
            print(f"The number was {random_number}, GAME OVER")
            break
        
        tries -= 1
        
adivinate_number()
        