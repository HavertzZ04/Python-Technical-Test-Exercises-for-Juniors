'''
Escribe un programa que cuente el número de vocales en una cadena de texto introducida por el usuario.
'''

def vocal_amount():
    text = input("Enter a string: ")
    
    vowels = "aeiouAEIOU"
    vowel_count = 0
    
    for i in text:
        if i in vowels:
            vowel_count += 1
            
    return vowel_count
    
print(vocal_amount())