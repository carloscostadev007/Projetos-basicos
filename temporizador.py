import time
t = input("Digite o tmepo (em segundos): ")
if t.isdigit():
    t = int(t)
else:
    print("Entrada inválida")
    quit()
while t != 0:
    minutos, segundos = divmod (t, 60)
    tempo = "{:02d}:{:02d}". format(minutos, segundos)
    print(tempo, end="\r") #parametro \r para sobrescrever
    time.sleep(1)
    t = t - 1
print("Tempo acabou!")

