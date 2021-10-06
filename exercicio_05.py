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
valorAumento=0
novoSalario=0
percAumento=0
# imprime='Salario atual: R$%.2f'%salario,'\nPercentual de aumento: ',percAumento,'\nValor do aumento: R$%.2f'%valorAumento,'\nNovo salario: R$%.2f'%novoSalario
if(salario<=280.00):
    percAumento='20%'
    valorAumento=(salario*(20/100))
    novoSalario=(salario+valorAumento)
    print('Salario atual: R$%.2f'%salario,'\nPercentual de aumento: ',percAumento,'\nValor do aumento: R$%.2f'%valorAumento,'\nNovo salario: R$%.2f'%novoSalario)
elif(salario<=700.00):
    percAumento='15%'
    valorAumento=(salario*(15/100))
    novoSalario=(salario+valorAumento)
    print('Salario atual: R$%.2f'%salario,'\nPercentual de aumento: ',percAumento,'\nValor do aumento: R$%.2f'%valorAumento,'\nNovo salario: R$%.2f'%novoSalario)
elif(salario<=1500.00):
    percAumento='10%'
    valorAumento=(salario*(10/100))
    novoSalario=(salario+valorAumento)
    print('Salario atual: R$%.2f'%salario,'\nPercentual de aumento: ',percAumento,'\nValor do aumento: R$%.2f'%valorAumento,'\nNovo salario: R$%.2f'%novoSalario)
else:
    percAumento='5%'
    valorAumento=(salario*(5/100))
    novoSalario=(salario+valorAumento)
    print('Salario atual: R$%.2f'%salario,'\nPercentual de aumento: ',percAumento,'\nValor do aumento: R$%.2f'%valorAumento,'\nNovo salario: R$%.2f'%novoSalario)


### FORMA MAIS CONVECIONAL PARA O EXERCICIO ACIMA
# CRIE AS VARIAVEIS: SALARIO, PERCENTUAL, AUMENTO E NOVOSALARIO
salario=float(input('Digite o valor do salario: '))
#verifique a condição
if(salario<=280.00):
    percentual=20
elif(salario<=700):
    percentual=15
elif(salario<=1500):
    percentual=10
else:
    percentual=5
print('Salario anterior: ', salario)
print('Percentual: ', percentual,'%')
# efetue os calculos
percentual=(percentual/100)
aumento=percentual*salario
novoSalario=aumento+salario
print('Aumento: R$%.2f'%aumento)
print('Novo salario: R$%.2f'%novoSalario)
