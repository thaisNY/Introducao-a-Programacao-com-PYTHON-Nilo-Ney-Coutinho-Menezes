deposito_inicial = float(input('Digite o deposito incial'))
taxa_juros = float(input('Digite a taxa de juros'))
dinheiro_conta = deposito_inicial
i = 0

while i < 24:
    i = i + 1
    if i == 1:
        print(f' Mes: {i} |  Saldo na conta: {deposito_inicial}')
    else:
        dinheiro_conta = (dinheiro_conta * taxa_juros) + dinheiro_conta
        print(f' Mes: {i} |  Saldo na conta: {dinheiro_conta}')