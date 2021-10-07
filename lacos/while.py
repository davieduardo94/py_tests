# Laço WHILE
# Seu formato é
#       while <teste>:
#           codigo1
#           codigo2
#           codigo3
            # ... 
#       codigo4

# "Crie um programa que imprima na tela os números 1 até o 10, usando o laço while
# Primeiro definimos nossa variável com valor 1.
numero = 1
# Depois testamos se ela é menor que 10. Como é, vai executar o laço while.
while(numero<=10):
    # Primeiro, imprime o valor da variável, que é 1
    print(numero)
    # Depois adiciona 1 a essa variável.
    numero += 1
    # e assim repete até que o teste seja false

# "Faça um programa que peça um número maior que 1 ao usuário. Em seguida, imprima todos os números, de 1 até o número que o usuário informou".

numero = 1
max = int(input('Digite um numero maior que 1: '))
while numero<=max:
    print(numero)
    numero+=1

# "Crie um programa que peça um número ao usuário e imprima todos os números pares de 1 até o número fornecido"
numero=1
max = int(input('Digite um numero: '))
while(numero<=max):
    if(numero%2==0):
        print(numero, end=" ")
    numero+=1

# "Escreva um programa que pede a senha ao usuário, e só sai do looping quando digitarem corretamente a senha"
senha = '2112'
tentativa = input('Digite sua senha: ')
while(senha!=tentativa):
    print('Senha incorreta!')
    tentativa = input('Digite sua senha: ')
print('Acesso liberado')
