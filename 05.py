'''
Escribe un programa que pida al usuario un número entero y calcule su factorial.
'''

def calculate_factorial():
    try:
        number = int(input("Enter a number to know its factorial: "))
        if number < 0:
            return "Factorial is not defined for negative numbers."
        
        total = 1
        for i in range(1, number + 1):
            total *= i
        return f"The factorial of {number} is {total}"
        
    except ValueError:
        return "Invalid Input, please enter a valid number"
    
print(calculate_factorial())