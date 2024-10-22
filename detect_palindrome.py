#Palíndromo é uma palavra, frase, número ou expressão que se mantém igual quando lida de trás para frente ou da esquerda para a direita. Por exemplo, as palavras "ovo" e "arara"

import math

def is_palindrome(word):
    j = len(word)-1
    result = 0
    for i in range(len(word)):
        if word[i] == word[j]:
            result = result + 1
        if i >= j:
            break
        j = j -1
    if result == math.ceil(len(word)/2):
        return True
    else:
        return False

words = ["arara","racecar","carro", "level"]

for word in words:
    print(word)
    print(is_palindrome(word))
    print("\n")

