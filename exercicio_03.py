# 1. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Digite uma letra: ')
if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u' or \
   letra=='A' or letra=='E' or letra=='I' or letra=='O' or letra=='U':
    print('É ma vogal! ', letra)
else:
    print('É uma consoante: ', letra)

# 2. Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:
#    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#    A mensagem "Reprovado", se a média for menor do que sete;
#    A mensagem "Aprovado com Distinção", se a média for igual a dez.
nota1 = float(input('Digite a nota1 de 0.0 - 10.0: '))
nota2 = float(input('Digite a nota2 de 0.0 - 10.0: '))
media = (nota1+nota2)/2
if media<7.0:
    print('Reprovado  media: ', media)
elif media>=7.0:
    print('Aprovado! media: ', media)
elif media==10:
    print('Super aprovado! media: ', media)
else:
    print('Fora de escala')

# 3. Faça um Programa que leia três números inteiros e mostre o maior deles.
num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))
maior=num1
# se o segundo for maior que a variavel, vai substituir ela
if (num2>maior):
    maior=num2
# se o terceiro for maior que a variavel, vai substituir ela
if (num3>maior):
    maior=num3
else:
    print('Todos iguais')
print('O maior é: ', maior)