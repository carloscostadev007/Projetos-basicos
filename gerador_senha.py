#funções

import random
import string

def password_generator(Len_pass = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options #concatenação de strings

    password_user = "" #string vazia
    for i in range(0, Len_pass):
        digit = random.choice(options)
        password_user = password_user + digit
    return password_user

choice_user = input("Quantos digitos você gostaria de gerar na na senha? ")

if choice_user.isdigit():       #verficação de entrada do usuário
    choice_user = int(choice_user)
else:
    print("Entrada inválida!")
    quit()
response = password_generator(Len_pass = choice_user)
print(f"Senha gerada:\n{response}")
