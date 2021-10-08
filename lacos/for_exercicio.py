# Faça um programa em Python que solicite um número positivo inteiro ao usuário, e depois exiba um tabuleiro na tela, com igual número de linhas e colunas.

print("Vamos criar um tabuleiro de tamanho:  N x N")
n=int(input("Valor de N: ") )

for linha in range(n):
    for coluna in range(n):
        print("x  ",end='')
    print()