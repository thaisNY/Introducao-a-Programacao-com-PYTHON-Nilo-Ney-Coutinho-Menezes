L = [15,7,27,39]

p = int(input("Digite o valor que procura: "))

x = 0
while x < len(L):
    if L[x] == p:
        print(f"{p} achado na posicao {x}")
        break
    x +=1

if x == len(L) and p not in L:
    print(f"{p} nao encontrado")

