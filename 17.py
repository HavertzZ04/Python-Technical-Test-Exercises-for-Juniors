'''
Escribe un programa que determine si dos palabras son anagramas (es decir, si tienen las mismas letras en un orden diferente).
'''

def anagram():
    word1 = sorted(list(input("Enter the first word: ")))
    word2 = sorted(list(input("Enter the second word: ")))
    
    if word1 == word2:
        return "This is an anagram"   
    else:
        return "This is not an anagram"            
        
print(anagram())