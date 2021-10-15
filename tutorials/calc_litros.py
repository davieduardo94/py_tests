print('Calculando litros e distancia em KM')
money = float(input('Quanto você tem? '))
vlrLitro = float(input('Qual o valor do Litro? '))
calc = money/vlrLitro
media = 13.2
distancia = media * calc
print('Voce pode comprar: %.3f'%calc, 'L e pode percorrer até: %.2f'%distancia, 'KM/L')
