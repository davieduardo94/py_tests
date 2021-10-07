# "Programe um script em Python que calcule a média de uma turma, não importa o número de alunos que ela tenha, seu único script serve para todos os casos"
alunos = int(input('Digite a quantidade de alunos: '))
count = 0
soma = 0
while(count<alunos):
    nota = float(input('Digite a nota do aluno: '))
    soma += nota 
    media = soma/alunos
    count+=1
    print('Soma:', soma, 'Aluno: ', count, 'Media da turma: ', media)


# media = nota /alunos

# Escreva um programa em Python que pede ao utilizador para introduzir um número inteiro, n, e calcula a soma
max = int(input('Digite um numero: '))
numero=1
anterior=0
while(numero<=max):
    if(numero>0):
        anterior=numero+anterior
        numero+=1
    else:
        print('Fim')
print(anterior)
