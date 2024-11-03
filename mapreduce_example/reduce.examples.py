from functools import reduce

numbers = [1, 2, 3, 4, 5]

def sum(a, b):
    print("a = ", a)
    print("b = ", b)
    print("a + b = ", a+b)
    return a+b
print(reduce(sum, numbers, 0)) #0 inicializador

#A função reduce em Python é usada para reduzir um iterável, como uma lista, a um único valor. Ela aplica uma operação em todos os elementos da lista, resultando em um único elemento. 
#A sintaxe da função reduce é objeto.reduce(função). No Python 2, a função reduce é built-in, mas no Python 3 ela está no módulo functools e é necessário um import para usá-la. 
#A função reduce pode ser usada para obter o produto ou o somatório dos itens de uma lista. Por exemplo, para encontrar o número máximo em uma lista, pode-se definir uma função find_max() que receba dois argumentos e retorne o maior deles. Em seguida, pode-se usar a função reduce() para encontrar o número máximo na lista. 