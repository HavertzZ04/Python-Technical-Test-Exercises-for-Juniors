'''
Escribe un programa que elimine los elementos duplicados de una lista introducida por el usuario.
'''

def remove_duplicates(user_list):
    return set(user_list)

print(remove_duplicates([23, "hola", True, True, "Hola", 22, 23, 6, 4]))