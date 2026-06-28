n = int(input("Digite o numero de elementos da primeira lista: "))
m = int(input("Digite o numero de elementos da segunda lista: "))
i = 0
lista1 = []
lista2 = []

while i < n:
    elemento1 = input("Digite o elemento a ser adicionado: ")
    i+= 1
    lista1.append(elemento1)

i = 0

while i < m:
    elemento2 = input("Digite o elemento a ser adicionado: ")
    i+= 1
    lista1.append(elemento2)

i = 0
lista3 = lista1[:]
lista3 += lista2
print(lista3)


