dist = int(input('Quantos kms vc vai percorrer '))
if dist> 0 and dist <= 200 :
    preco = dist * 0.5
    print(f'Voce vai pagar {preco}')

elif dist >200:
    preco = dist * 0.45
    print(f'Voce vai pagar {preco}')

else:
    print('Voce nao ira viajar')