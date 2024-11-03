
import json
from functools import reduce


f = open("./mapreduce_example/aquarium.json", encoding="utf8")
data_aquarium = json.load(f)
animals =  data_aquarium["data"]

def pick_animal_type(animal):
    return animal["type"], 1

def reducer(acc, val):
    if val[0] not in acc.keys():
        acc[val[0]] = 0 + val[1]
    else:
        acc[val[0]] = acc[val[0]] + val[1]
    return acc

type_animals = list(map(pick_animal_type, animals))
print(type_animals)
animals_type_count = reduce(reducer, type_animals, {})
print(animals_type_count)

#Em Python, uma tupla é uma estrutura de dados que armazena um conjunto de valores de forma imutável, ou seja, não é possível alterar os elementos de uma tupla após a sua criação: 
#Para criar uma tupla, basta listar os valores separados por vírgulas, e opcionalmente, entre parênteses. 
#Uma tupla vazia é criada com (). 
#Uma tupla com um único elemento é criada com (elemento,). 
#Tuplas com mais de um elemento são criadas com (elemento1, elemento2, ...). 
#As tuplas são úteis para guardar dados protegidos, como registros, que não devem ser alterados. 
#Algumas características das tuplas em Python são:
#Possuem funções embutidas para realizar operações, como concatenação, indexação e contagem de elementos. 
#A função id() permite verificar o ID (identificação) da tupla na memória. 
#É possível desempacotar os valores e atribuí-los a variáveis individuais. 
#Tuplas têm um tempo de processamento mais rápido. 