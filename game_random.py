###biblioteca importada###
import random
###Mensagem de inicio###
print ("Seja bem vindo(a), ao Game Random!")
name = input ("Digite seu nome: ")
print (f"vamos ao game {name}, iniciando em instantes...")

###inicio do game, escolha de teto do game, ex: de 0 até 100###
choice_number = input("Digite o número teto do desafio: ")
###Verfificação para saber se a variável do usuário é um número inteiro### 
if choice_number.isdigit():###concidicional "if" e função combinada "isdigit" para verificar se realmente é um número, se for um numero ele retorna verdadeiro, se for caractere devolde falso###
   choice_number =  int(choice_number)
else:
   print("Erro: valor informado não é numérico, execute novamente  e informe um número!")
   quit()###encerra execuçaõ do programa###

random_number = random.randint(0, choice_number)###linha de código que gera o número randomico de 0 ao número teto coloocado pelo usuário###

### bloco estruturado para checar se o que foi digitado pelo usuário é númerico ou caractere, tambémm da dicas para o usuário caso ele tenha chutado valor abaixo ou acima do numero randomico gerado pelo programa, auxuliando o usuário, adionei tbm um contador de tentativas###
n_choices = 0
while True:
  answer_user = input("adivinhe o número: ")
  if answer_user.isdigit():
     answer_user = int(answer_user)
  else:
     print("Erro: valor infromado não é númerico, informe um número")
     continue
  n_choices = n_choices + 1
  if answer_user == random_number:
     print("Acertou, meus parabéns!")
     break
  elif answer_user > random_number:
     print("Chutou alto, o número randomico é menor")
  else:
   print("chutou baixo, número randomico é maior...")
###foi usado o + para fazer a concatenação e o comadno str(variavel)###
print("Número de Tentativas: " + str (n_choices))


      

     
  




