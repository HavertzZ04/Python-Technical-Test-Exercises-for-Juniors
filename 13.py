'''
Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit y viceversa.
'''

def celsius_to_fahrenheit(temperature):
    return f"{temperature} Celsius Degree is {(temperature * 9 / 5) + 32:.2f} Fahrenheit\n"

def fahrenheit_to_celsius(temperature):
    return f"{temperature} Fahrenheit Degree is {(temperature - 32) * 5 / 9:.2f} Celsius\n"

def get_temperature():
    while True:
        try:
            temperature = float(input("\nEnter the temperature for your option: "))
            return temperature
        except ValueError:
            print("Invalid input, please enter a valid temperature.")

def converter():
    while True:
        print("<- Temperature Converter ->")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("0. Exit")
        
        try:
            option = int(input("Your answer here: "))
        except ValueError:
            print("Invalid input, please enter a valid option.\n")
            continue
            
        if option == 0:
            print("Bye, bye")
            break
        elif option == 1:
            temperature = get_temperature()
            print(celsius_to_fahrenheit(temperature))
        elif option == 2:
            temperature = get_temperature()
            print(fahrenheit_to_celsius(temperature))
        else:
            print("Enter a valid number")
                
converter()

    