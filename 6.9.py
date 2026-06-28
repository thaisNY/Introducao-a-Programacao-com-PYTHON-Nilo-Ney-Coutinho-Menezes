#Modifique pra procurar 2 valores 
#Na impressao indique quais dos 2 valores foi achado primeiro

L = [15,7,27,39]

p = int(input("Digite o valor que procura: "))
q = int(input("Digite o segundo valor que procura: "))
x = 0
posp = 0
posq = 0
while x < len(L):
    if L[x] == p:
        print(f"{p} achado na posicao {x}")
        posp = x
        
    if L[x] == q:
        print(f"{q} achado na posicao {x}")
        posq = x
    x +=1

if x == len(L) and p not in L:
    print(f"{p} nao encontrado")

if x == len(L) and q not in L:
    print(f"{q} nao encontrado")

if p in L and q in L:
    if posp < posq:
        print(f"{p} foi achado primeiro na posicao {posp}")
    elif p == q:
        print("Ambos sao iguais achados na mesma posicao")
    elif posp > posq:
         print(f"{q} foi achado primeiro na posicao {posq}")