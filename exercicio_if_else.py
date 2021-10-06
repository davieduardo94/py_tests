###     Faça um programa que peça dois números e imprima o maior deles.
print('Qual o maior?\n')
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
if num1>num2:
    print('num1 é maior:', num1)
else:
    if num2>num1:
        print('Num2 é maior:', num2)
    else:
        print('iguais')

##       Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo.
numero = int(input('Digite um numero: '))
if numero>=0:
    print('O numero:', numero, 'é positivo')
else:
    print('O numero: ', numero, 'é negativo')