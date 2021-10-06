#7. Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#  Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print('Selecione o Turno:')
print('M - matutino')
print('V - vespertino')
print('N - noturno')
turno=input('Digite o codigo do turno: ')

### NESSA PRIMEIRA FORMA COM APENAS 'IF' SERA CHECADO LINHA POR LINHA, MESMO QUE A CONDIÇÃO JA TENHA SIDO SATISFEITA
# PROBLEMAS: PERCA DE DESEMPENHO NO SOFTWARE
if(turno=='M'):
    print('Bom dia')
if(turno=='V'):
    print('Boa tarde')
if(turno=='N'):
    print('Boa noite')

### codigo para verificar o desempenho
#NESSA ASSIM QUE A CONDIÇÃO FOR VERDADEIRA, A EXECUÇÃO É ENCERRADA.
# VANTAGEM: TEMPO DE EXECUÇÃO MENOR E MAIOR DESEMPENHO
elif(turno=='M'):
    print('Bom dia')
elif(turno=='V'):
    print('Boa tarde')
elif(turno=='N'):
    print('Boa noite')
else:
    print('Valor invalido')


#8. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    # salários até R$ 280,00 (incluindo) : aumento de 20%
    # salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    # salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    # salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
        # o salário antes do reajuste;
        # o percentual de aumento aplicado;
        # o valor do aumento;
        # o novo salário, após o aumento.
salario=float(input('Digite o valor do salario: '))
if(salario<=280.00):
    salario=salario+(salario*(20/100))
    print('Salario:', salario)
elif(salario>280.00) and (salario<=700.00):
    salario=salario+(salario*(15/100))
    print('Salario:', salario)
elif(salario>700.00) and (salario<=1500.00):
    salario=salario+(salario*(10/100))
    print('Salario:', salario)
elif(salario>1500.00):
    salario=salario+(salario*(5/100))
    print('Salario:', salario)