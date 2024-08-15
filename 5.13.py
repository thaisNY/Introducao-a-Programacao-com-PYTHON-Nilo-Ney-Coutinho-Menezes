#numero de meses para pagar a divida
#total de juros pagos
#total pago

divida = float(input('Digite o valor incial'))
taxa_juros = float(input('Digite a taxa de juros ao mes'))
pago_mes = float(input('Quanto vode pode pagar no mes'))

n_meses = 0

while divida > 0:
    divida = (divida + taxa_juros*divida) - pago_mes
    n_meses += 1
    print(f'Mes `{n_meses} o valor da sua divida neste mes eh {divida}')

print(f'A divida foi paga em {n_meses} meses')

