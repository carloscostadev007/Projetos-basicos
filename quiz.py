print ("Seja bem vindo ao quiz Tech")
nome_usuario = input("Digite seu nome: ")

resposta_usuario = input(f"{nome_usuario}, você gostaria de inciar o Quiz? (S/N): ")


if resposta_usuario != "S":
    quit()

score = 0

##estrutura pergunta 1##
print("Iniciando...")
print("Qual foi o primeiro sistema operacional desenvolvido pela Microsoft? \n (a) Windows XP \n (b) MS-DOS \n (c) Linux \n (d) MacOS\n")
resposta_1 = input("Resposta: ")

if resposta_1 == "b":
    print("correto!")
    score =  score + 1
else:
    print("incorreto")

##estrutura pergunta 2##
print("O que é a 'nuvem' na computação em nuvem? \n (a) Um servidor físico na sua empresa \n (b) Um conjunto de servidores remotos que armazenam e processam dados pela internet \n (C) Um aplicativo para armazenar fotos\n \n(D) Uma rede local de computadores \n")
resposta_2 = input("Resposta: ")

if resposta_2 == "b":
    print("correto!")
    score =  score + 1
else:
    print("incorreto")


##estrutura pergunta 3##
print("Qual empresa é conhecida por criar o sistema operacional Android? \n (a) Apple \n (b) Microsoft \n (c) Google \n (d) Samsung \n")
resposta_3 = input("Resposta: ")

if resposta_3 == "c":
    print("correto!")
    score =  score + 1
else:
    print("incorreto")

##estrutura pergunta 4##
print("O que significa a sigla 'AI' na área de tecnologia? \n (a) Artificial Intelligence (Inteligência Artificial) \n (b) Automated Integration \n (c) Analytical Input \n (d) Advanced Interface \n")
resposta_4 = input("Resposta: ")

if resposta_4 == "a":
    print("correto!")
    score =  score + 1
else:
    print("incorreto")

##estrutura pergunta 5##
print("Qual é o protocolo principal usado para transferir dados na web? \n (a) FTP \n (b) DNS \n (c) HTTP \n (d) SMTP \n")
resposta_5 = input("Resposta: ")

if resposta_5 == "c":
    print("correto!")
    score =  score + 1
else:
    print("incorreto")


print(f"Parabéns...sua pontuação é: {score}/5")










