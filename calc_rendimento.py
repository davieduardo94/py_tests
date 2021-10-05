#!/usr/bin/env python
# coding: utf-8
print('Calculadora de rendimentos')
valorInicial= float(input('Digite o valor inicial do investimento: '))
rentabilidade = float(input('% de rentabilidade: '))
rentabilidade = rentabilidade/100
meses = int(input('Quantidade de meses: '))
valorfinal = valorInicial*(1+rentabilidade)**meses
print('O rendimento da sua aplicação com base em ', meses,'meses, com uma taxa de ',rentabilidade,'% será de: ',valorfinal)



