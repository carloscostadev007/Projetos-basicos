import json

f = open("./Aquario/aquarium.json", encoding="utf8")
data_aquarium = json.load(f)
animals = data_aquarium["data"]
def verify_fish(animal):
    if animal["type"] == "fish":
        return True
    return False
animals_fish = list(filter(verify_fish, animals))
def animal_name(animal):
    return animal["name"]
animals_fish_name = list(map(animal_name, animals_fish))
print(animals_fish_name)
def assign_to_tank(animals, names_selected, new_tank_number):
    def change_tank_number(animal):
        if animal["name"] in names_selected:
            animal["tank number"] = 42
        return animal
    return list(map(change_tank_number, animals)) 
new_aquarium = assign_to_tank(animals, animals_fish_name, 42)
print(new_aquarium)

#Função filter
#Em Python filtra elementos de uma sequência com base em uma condição específica. Para isso, ela utiliza uma função que retorna True ou False para um determinado argumento de entrada. A função filter é útil quando se trabalha com um grande volume de informações, como listas, dicionários e tuplas. Ela permite filtrar por tipo ou aplicar edições. Para usar a função filter, é preciso passar a função sem os parênteses e a lista onde a aplicação será feita. O resultado será mostrado como lista do Python. 

#Função lambda
#Em Python é uma forma de criar funções anônimas, ou seja, sem a necessidade de defini-las explicitamente. Elas são uma ferramenta útil para criar funções simples, que serão utilizadas apenas uma vez e não precisam ser reutilizadas em outro lugar do código. 
#A estrutura de uma expressão lambda é simples e começa com a palavra-chave lambda, seguida por parâmetros, dois pontos e, por fim, uma expressão que a função retorna. 

#Por exemplo, lambda x: x + 2 é uma função lambda.

#animals_fish = list(filter(lambda animal:(animal["type"] == "fish"), animals))

#Função map
#Em Python é uma função built-in que permite aplicar uma função a todos os itens de uma sequência (como uma lista) e retornar uma nova sequência com os resultados.