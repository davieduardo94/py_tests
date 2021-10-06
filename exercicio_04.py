# 4. Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.
num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))
maior=num1
menor=num1
if (num2>maior):
    maior=num2
if(num2<menor):
    menor=num2
# se o terceiro for maior que a variavel, vai substituir ela
if (num3>maior):
    maior=num3
if(num3<menor):
    menor=num3
else:
    print('Todos iguais')
print('O maior é: ', maior, 'e o menor é: ', menor)

# 5. Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na tela
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
troca=num2
num2=num1
num1=troca
print('numero1: ', num1)
print('numero2: ', num2)

#  forma mais clean para o exercicio 5
v1 = input('Digite o numero: ')
v2 = input('Digite o numero: ')
[v1, v2] = [v2, v1]
print('Primeiro numero ',v1)
print('Segundo numero', v2)

#6. Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))
aux=0
#menor=num1

if(num3>num2):
    aux=num3
    num3=num2
    num2=aux
if(num2>num1):
    aux=num2
    num2=num1
    num1=aux
if(num3>num2):
    aux=num3
    num3=num2
    num2=aux
    print('O maior é: ', num1, 'o do meio é: ',num2, 'o menor é: ',num3)
else:
    print('Todos iguais')
