# Comando return - O que é? Para que serve?
# Fazer tarefas específicas (de preferência, da maneira mais clara e concisa o possível)
# Se comunicar com outras partes do programa
#    def nome_funcao(parâmetros):
#       código
#       código
#       código
#       ...
#       return algo

# A única coisa nova e diferente, é a última linha da função:
# return alg

# Crie um programa em Python que peça o nome e o sobrenome de uma pessoa, depois exiba na tela a mensagem "Olá sobrenome, nome".
nome = input('Digite o nome: ')
sobrenome = input('Digite o sobrenome: ')

def invert(nome, sobrenome):
    return (sobrenome+', '+nome)

print(invert(nome, sobrenome))


# Crie um programa em Python que diz se o número inserido pelo usuário é par ou ímpar. 
# Ele deve fazer isso através de uma função que recebe o inteiro e retorna True ou False.

numero = int(input('Digite um numero: '))
def parImpar(num):
    if(num%2):
        return(True)
    else:
        return(False)

parImpar(numero)


# Como retornar mais de um valor
# Para isso, basta separar cada informação por vírgula.

def cadastro():
    name = input('Digite o nome: ')
    age = int(input('Digite sua idade: '))
    return(name, age)


nome, idade = cadastro()
print('Cadastro realizado com sucesso!')
print('Seu nome:',nome, 'sua idade: ',idade)

