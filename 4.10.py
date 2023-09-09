op = (input('Digite R para consumo residencial, I para consumo industrial, e C para comercial')).upper()
consumo = int(input('Digite o valor do consumo  em kwh'))
if op == 'R':
    if consumo < 500:
        preco = consumo*0.40
        print(f'Voce consumiu {consumo} e ira pagar {preco} reais')
    else:
        preco = consumo * 0.65
        print(f'Voce consumiu {consumo} e ira pagar {preco} reais')

elif op == 'C':
    if consumo < 1000:
        preco = consumo*0.55
        print(f'Voce consumiu {consumo} e ira pagar {preco} reais')
    else:
        preco = consumo * 0.60
        print(f'Voce consumiu {consumo} e ira pagar {preco} reais')

elif op == 'I':
    if consumo < 5000:
        preco = consumo*0.55
        print(f'Voce consumiu {consumo} e ira pagar {preco} reais')
    else:
        preco = consumo * 0.60
        print(f'Voce consumiu {consumo} e ira pagar {preco} reais')

