n1 = int(input('Digite o valor do primeiro'))
n2 = int(input('Digite o valor do segundo'))

i = 1
resp = 0
while i <= n2:
    resp = resp + n1
    i = i + 1
print(f'{n1} x {n2} = {resp}')