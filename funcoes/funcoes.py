# Função - Como Declarar, Chamar e Usar funções
# O escopo da declaração de uma função é:

#    def nome-funcao(argumentos):
#       código
#       código
#       ...
#       return valor

# Há duas coisas opcionais:
# Argumentos (informações que você passa para a função, ao chamar ela)
# Retornar valor (informações que a função retorna para quem chamou ela)

def soma(num1,num2):
    print('A soma é:',(num1+num2))

def subtracao(num1,num2):
    print('Subtracao: ',(num1-num2))

def multiplicacao(num1,num2):
    print('Multiplicacao: ',(num1*num2))

def divisao(num1,num2):
    print('Divisao: ',(num1/num2))

operacao = input('Digite qual a operacao + - / *: ')
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
if(operacao=='+'):
    soma(num1,num2)
elif(operacao=='-'):
    subtracao(num1,num2)
elif(operacao=='/'):
    divisao(num1,num2)
elif(operacao=='*'):
    multiplicacao(num1,num2)
