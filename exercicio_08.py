# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
import math
a = int(input('Digite o valor de a: '))
if(a==0):
    print('A equação não é do segundo grau! \nFIM.')
else:
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))
    delta = (b*b)-4 *(a*c)
    x1= (-b + math.sqrt(delta))/(2*a)
    x2= (-b - math.sqrt(delta))/(2*a)
    if(delta<0):
        print('O valor de delta é negativo: ',delta,'\nFIM')
    elif(delta==0):
         print('A equação possui uma raiz real: ', delta,'raiz x1: ', x1)
    else:
        print('A equação possui duas raizes reais', delta, 'raiz x1: ', x1, 'raiz x2: ', x2)
