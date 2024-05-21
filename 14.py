'''
Escribe un programa que pida al usuario una frase y cuente el número de palabras que contiene.
'''


def count_words():
    phrase = input("Enter a text: ") 
    words = phrase.split()
    return len(words)

print(count_words())