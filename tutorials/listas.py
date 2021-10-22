# O que define uma lista nada mais é que um par de colchetes: [ ]
# Chamamos de item os dados contidos em uma lista.
# Os itens são sempre separados por vírgula,

# Crie um programa em Python que peça seu nome, sua idade, sua altura, seu peso e True se for casado ou False para solteiro.
# Em seguida, ele deve armazenar todas essas informações numa lista chamada eu. Por fim, imprima essa lista na tela.

# nome = str(input('Digite seu nome: '))
# idade = int(input('Digite sua idade: '))
# altura = float(input('Digite sua altura: '))
# peso = int(input('Digite seu peso: '))
# estado = int(input('Estado civil: \n1 - Solteiro \n2 - Casado: '))

# estado = False if (estado==1) else True

# eu =[nome, idade, altura, peso, estado]
# print('Nome:', eu[0])
# print('Idade: ', eu[1])
    
# Adicionar Item em uma lista: append()

bandas = []
print(bandas)
while True:
    op =int(input("1. Adicionar banda\n"
                  "2. Exibir bandas favoritas\n"
                  "3. Tamanho da lista\n"
                  "4. Mudar valor de item\n"))

    if(op==1):
        banda=input("Digite nome da banda: ")
        bandas.append(banda)
    if(op==2):
        print(bandas)
    if(op==3):
        print("Tamanho da lista: ", len(bandas))
    if(op==4):
        index=int(input("Indice que vai alterar: "))
        if(index<len(bandas)):
            temp=input("Nome da banda: ")
            bandas[index] = temp
        else:
            print("Esse indice nao existe")