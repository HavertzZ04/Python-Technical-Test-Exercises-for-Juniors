'''
Escribe un programa que pida al usuario un número entero y determine si es par o impar.
'''

def even_or_odd():   
    try: 
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            return f"The number {number} is even"
        else:
            return f"The number {number} is odd"
        
    except ValueError:
        return "Invalid number, try again"
         
print(even_or_odd())