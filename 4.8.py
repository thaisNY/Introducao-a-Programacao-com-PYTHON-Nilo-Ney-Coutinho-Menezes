a = int(input('Digite o primeiro valor'))
b = int(input('Digite o segundo valor'))

op = (input('Digite + para somar, - para subtrair, * para multiplicar e / para divisao'))

if op == '+':
    res = a + b
    print(f'{a} {op} {b} = {res}')
elif op == '-':
    res = a - b
    print(f'{a} {op} {b} = {res}')

elif op == '*':
    res = a * b
    print(f'{a} {op} {b} = {res}')

elif op == '/':
    res = a / b
    print(f'{a} {op} {b} = {res}')

