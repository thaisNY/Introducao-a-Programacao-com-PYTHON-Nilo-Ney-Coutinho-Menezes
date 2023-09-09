valorCasa = float(input('Digite o valor da casa'))
sal = float(input('Digite o seu salario'))
ano = float(input('Digite em quantos anos voce quer pagar'))

prest = (valorCasa)/12*ano
if prest >= sal*0.3:
    print('Voce nao pode financiar a casa')
else:
    print(f'O valor da parcela sera {prest}')