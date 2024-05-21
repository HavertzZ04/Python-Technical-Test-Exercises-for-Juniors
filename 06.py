'''
Escribe un programa que pida al usuario una palabra y determine si es un palíndromo (una palabra que se lee igual de izquierda a derecha que de derecha a izquierda).
'''

def palindrome():
    word = input("Enter a word to see if it is a palindrome: ").lower()
    if word == word[::-1]:
        return f"The word {word} is a palindrome"
    else:
        return f"The word {word} is not a palindrome"
    
print(palindrome())