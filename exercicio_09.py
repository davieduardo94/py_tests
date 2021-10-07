ano = int(input('Digite um ano no formato aaaa: '))
if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('Ano bissexto: ', ano)
else:
    print('Não é bissexto ', ano)

#  Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))
valida = False
# verificar se o mes tem 31 dias
if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
    # verificando se o dia é menor ou igual a 31
    if(dia<=31):
        valida=True
#verificar meses com 30 dias
elif(mes==4 or mes==6 or mes==9 or mes==11):
    # verificar se o dia é menor ou igual a 30
    if(dia<=30):
        valida=True
elif(mes==2):
    # verificar se é ano bissexto
    if(ano%4==0 and ano %100!=0) or (ano % 400 == 0):
        if(dia<=29):
            valida=True
    elif(dia<=28):
            valida=True
if(valida):
    print('Data valida: ',dia,'/', mes,'/', ano)
else:
    print('Data invalida')