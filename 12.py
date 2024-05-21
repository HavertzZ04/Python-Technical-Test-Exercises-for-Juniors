'''
Escribe un programa que simule una calculadora básica, permitiendo al usuario elegir entre suma, resta, multiplicación y división.
'''

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero."
    return n1 / n2

def get_numbers():
    while True:
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
            return number1, number2
        except ValueError:
            print("Invalid input, please enter valid numbers.")

def calculator():
    while True:
        print("\n<- Select one of the options ->")
        print("1. Sum")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("0. Exit")

        try:
            option = int(input("Your choice: "))
        except ValueError:
            print("Invalid input, please enter a valid option.")
            continue

        if option == 0:
            print("Have a good day, bye!")
            break
        elif option in (1, 2, 3, 4):
            n1, n2 = get_numbers()
            if option == 1:
                result = add(n1, n2)
            elif option == 2:
                result = subtract(n1, n2)
            elif option == 3:
                result = multiply(n1, n2)
            elif option == 4:
                result = divide(n1, n2)

            print(f"Result: {result}")
        else:
            print("Invalid option, try again.")

calculator()
