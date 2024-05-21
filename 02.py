'''
Escribe un programa que pida al usuario dos números y luego imprima la suma de estos.
'''


def sum_numbers():
    print("We are gonna sum 2 numbers :)")
    try:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        return f"The sum of the numbers is: {number1 + number2}"
        
    except ValueError:
        return "Invalidad input, please enter valid numbers"

print(sum_numbers())