#Digite numeros ate digitar 0
#soma dos nums
#media aritimetica

soma = 0
mediaA = 0
i = 0
while True:
    num = int(input("Digite um numero"))
    soma += num
    i += 1
    if num == 0:
        break

mediaA = soma/i
print(f'Voce digitou {i} numeros ')
print(f'A soma foi {soma}')
print(f'A media aritimetiaca foi {mediaA}')