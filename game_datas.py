#Json é um arquivo que armazena uma estrutura de dicionário usando {} e valores dentro dela

import json
import random

#open função especial do Python para abrir arquivos json
f = open("words.json", encoding="utf8")

words = json.load(f)#Carregar dados dentro do Json, função load para tarzer um arquivo
print(words.keys())
choice_c = random.choice(list(words.keys()))

print("Olá seja bem vindo!")
print("############################")

n_choices = 5
win = False
while n_choices > 0 and win is not True:
    print("Dica: " + words[choice_c])
    answer_user = input("Data: DDMMAAAA\n")
    print("################\n")
    if len(answer_user) != 8:    #Verificação de tamanho
        print("Erro na entrada. A resposta deve conter 8 digítos.")
        continue
    if answer_user.isdigit():
        check = []
        pontuation = 0
        for i in range(8):
            if answer_user[i] == choice_c[i]:
                check.append("👍")
                pontuation = pontuation + 1
            if pontuation == 8:
                win = True
            else:
                check.append("😒")
        print("Resposta: \n")
        print("|".join(check))
        print("|".join(answer_user))
        print("################\n")
    else:
        print("Erro na entrada.  A respota deve ser uma data!")
        continue
    n_choices = n_choices - 1

if win == True:
    print("Vitória!")
else:
    print("Derrota!")
    print("A respota é: " + choice_c)