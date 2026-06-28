
#Percorra 2 listas e gere uma terceira sem elementos repetidos

lista1 = [1,21,1,3,3,-1,'abc', 'd',12] #9
lista2 = [1,2,3,4,'d',5.3] #6

lista3 = lista1 + lista2

lista4 = []
for elemento in lista3:
    if elemento not in lista4:
        lista4.append(elemento)
    

print(lista4)
#lista3 = list(set(lista1 + lista2))