sal = float(input('Digite o seu salario'))
if sal > 1250:
    novosal = sal * 1.1
    print(f'O novo salario eh {novosal}')
else :
    novosal = sal * 1.15
    print(f'O novo salario eh {novosal}')