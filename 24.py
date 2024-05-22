'''
Escribe un programa que duplique cada carácter de una cadena introducida por el usuario.
'''

def duplicate_character():
    text = input("Enter a string: ")
    
    duplicate_list = [i * 2 for i in text]
    return "".join(duplicate_list)
        
print(duplicate_character())