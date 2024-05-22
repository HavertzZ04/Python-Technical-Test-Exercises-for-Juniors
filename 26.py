'''
Escribe un programa que encuentre la palabra más larga en una frase introducida por el usuario.
'''

def largest_word():
    phrase = input("Enter a phrase: ").split(" ")
    
    word = ""
    for i in phrase:
        if len(i) > len(word):
            word = i
    return word

print(largest_word())
    
    