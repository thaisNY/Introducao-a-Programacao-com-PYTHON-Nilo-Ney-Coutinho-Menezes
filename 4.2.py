vel = float(input('Digite a velocidade do carro'))
if vel > 80:
    multa = (vel - 80)*5
    print(f'Voce foi multado no valor de {multa} reais')