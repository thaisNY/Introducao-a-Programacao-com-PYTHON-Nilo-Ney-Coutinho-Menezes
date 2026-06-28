nota = [0,0,0,0,0,0,0]
soma = 0
x = 0

while x < 7:
    nota[x] = float(input("Digite a nota: "))
    soma+=nota[x]
    x+=1

x = 0
print(f"A media eh {soma/7}")
while x < 7:
    print(f"a nota de indice {x + 1} eh {nota[x]}")
    x+=1