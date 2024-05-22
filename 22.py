'''
Escribe un programa que pida una lista de palabras al usuario y las ordene alfabéticamente.
'''

def order_list():
    words = input("Enter a list of words separated by commas: ")
    words_list = [i.strip() for i in words.split(',')]
    
    return sorted(words_list)

print(order_list())