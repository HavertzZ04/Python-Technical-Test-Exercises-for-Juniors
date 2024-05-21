'''
Escribe un programa que pida al usuario una lista de números separados por comas y luego imprima la lista en orden ascendente.
'''

def order_numbers():
    try: 
        number_list = input("Enter a list of numbers separtes by commas: ")
        number_list = [int(num) for num in number_list.split(",")]
        return sorted(number_list)
    
    except ValueError:
        return "Invalid input, please enter a list of number separate by commas"

print(order_numbers())  