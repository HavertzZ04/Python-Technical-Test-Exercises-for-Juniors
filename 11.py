'''
Escribe un programa que pida al usuario tres números y determine cuál es el mayor y cuál es el menor.
'''

def mayor_minor():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    n3 = int(input("Enter the last number: "))
    
    number_list = [n1, n2, n3] 
    
    return f"Mayor number: {max(number_list)}\nMinor number: {min(number_list)}"

print(mayor_minor())