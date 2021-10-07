#  Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
print('1 - Domingo')
print('2 - Segunda')
print('3 - Terca')
print('4 - Quarta')
print('5 - Quinta')
print('6 - Sexta')
print('7 - Sabado')
dia = int(input('Escolha o dia da semana:'))
if(dia==1):
    print('Domingo')
elif(dia==2):
    print('2 - Segunda')
elif(dia==3):
    print('3 - Terca')
elif(dia==4):
    print('4 - Quarta')
elif(dia==5):
    print('5 - Quinta')
elif(dia==6):
    print('6 - Sexta')
elif(dia==7):
    print('7 - Sabado')
else:
    print('Dia invalido.')

# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
nota1 = float(input("Digite a nota de 0.0 a 10.0: "))
nota2 = float(input("Digite a nota de 0.0 a 10.0: "))
media = (nota1+nota2)/2

if (media<4.0):
    print("Nota E, REPROVADO \nnota1: ", nota1,"\nnota 2: ",nota2, "\nnota final: ", media)
elif (media>4.0) and (media<6.0):
    print("Nota D, REPROVADO \nnota1: ", nota1,"\nnota 2: ",nota2, "\nnota final: ", media)
elif (media>6.0) and (media<7.5):
    print("Nota C, APROVADO, nota1: ", nota1," nota 2: ",nota2, " nota final: ", media)
elif (media>7.5) and (media<9.0):
    print("Nota B, APROVADO nota1: ", nota1," nota 2: ",nota2, " nota final: ", media)    
# elif (media>9.0) and (media<=10.0):
else:
    print("Nota A, APROVADO nota1: ", nota1," nota 2: ",nota2, " nota final: ", media)

# Faça um Programa que peça os 3 lados de um triângulo. 
# O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.,

a=int(input('Digite o valor do lado1: '))
b=int(input('Digite o valor do lado2: '))
c=int(input('Digite o valor do lado3: '))
if((a+b)<c) and ((a+c)<b) and ((b+c)<a):
    print('Nao é um triangulo')
elif(a==b) and (a==c):
    print('Triangulo equilatero')
elif(a==b) or (a==c) or (b==c):
    print('Triangulo Isoceles')
else:
    print('Triangulo Escaleno')