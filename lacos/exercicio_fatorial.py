numero = int(input('Digite um numero inteiro e positivo: '))
while(numero!=0):
    resultado=1
    for var in range(1,numero+1):
        resultado *= var
    print(resultado)
    numero = int(input('Digite um numero inteiro e positivo: '))
else:
    print('Fim do programa!')
