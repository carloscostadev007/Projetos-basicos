
operacao = input("Escolha o tipo de operação que deseja fazer:\nA: Adição\nS: Subtração\nM: Multiplicação\nD: Divisão\nQ: Sair\n").lower()
if operacao == 'q':
    print("Adeus!")
    quit()    
if operacao == "a":
    #Adição
    a = input('Digite o 1a valor de: ')
    b = input('Digite o 2a valor de: ')
    soma = float(a) + float(b) #não esquecer de declarar as var em (int/float)
    print(f'Resultado da soma é: {soma}')
elif operacao == "s":
    #Subtração
    a = input('Digite o 1a valor de: ')
    b = input('Digite o 2a valor de: ')
    sub = float(a) - float(b) #não esquecer de declarar as var em (int/float)
    print(f'Resultado da subtração é: {sub}')
elif operacao == "m":
    #Multiplicação
    a = input('Digite o 1a valor de: ')
    b = input('Digite o 2a valor de: ')
    mult = float(a) * float(b) #não esquecer de declarar as var em (int/float)
    print(f'Resultado da multiplicação é: {mult}')
else:
    operacao == "d"
    #Divisão
    a = input('Digite o 1a valor de: ')
    b = input('Digite o 2a valor de: ')
    div = float(a) / float(b) #não esquecer de declarar as var em (int/float)
    print(f'Resultado da divisão é: {div}')
