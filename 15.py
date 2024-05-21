'''
Escribe un programa que calcule la media de una lista de números introducida por el usuario.
'''

def calculate_media():
    numbers = input("Enter a list of numbers separated by commas: ")
    
    numbers_list = [float(number.strip()) for number in numbers.split(",")]
    answer = sum(numbers_list) / len(numbers_list)
    return f"The mean of your numbers is: {answer}"
    
print(calculate_media())