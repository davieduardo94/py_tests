vlr_hora = float(input('Digite o valor da hora: '))
qtd_hora = int(input('Digite a quantidade de horas: '))
salario_bruto = (vlr_hora * qtd_hora)
if(salario_bruto<=900):
    IR=0
elif(salario_bruto<=1500):
    IR=5
elif(salario_bruto<=1500):
    IR=10
else:
    IR=20

descontoIR = (salario_bruto * (IR/100))
INSS = salario_bruto * 0.10
fgts = (0.11 * salario_bruto)
sindicato = (0.03 * salario_bruto)
total_descontos = (descontoIR + INSS + sindicato)
salario_liquido = (salario_bruto - total_descontos)
print('IR: ', descontoIR)
print('INSS: ', INSS)
print('FGTS: ', fgts)
print('Sindicato: ', sindicato)
print('Total descontos: ', total_descontos)
print('Salario liquido: ', salario_liquido)
