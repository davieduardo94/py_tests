#   for <item> in <conjunto_de_itens>:
#       <bloco_de_codigo>
# item: corresponde a cada elemento presente na variável que permite a iteração;
# conjunto_de_itens: pode ser uma lista, uma string, uma tupla, um dicionário ou um objeto que permita iterações.

# Por padrão, a estrutura de repetição só termina depois de ler o último elemento da variável iterável. 
# Entretanto, é possível modificar essa condição e interromper o loop no meio do caminho. 
# Para isso, utilizamos a instrução break, que encerra a execução do loop ao encontrar uma condição específica
# Devemos utilizar a instrução break em conjunto com uma estrutura condicional, como a if/else ou até mesmo com outro laço de repetição for.
#
# for <item> in <conjunto_de_itens>:
#    <bloco_de_codigo>
#    if <condicao_verdadeira>:
#         <outras_instrucoes>
#         break

pessoas = [
        (
            {
                'nome': 'João', 
                'cidade': 'Belo Horizonte'
            }
        ),
        (
            {
                'nome': 'Maria', 
                'cidade': 'São Paulo'
            }
        ),
        (
            {
                'nome': 'Pedro', 
                'cidade': 'Curitiba'
            }
        )
]
contador = 0
for pessoa in pessoas:
    contador += 1
    print(contador)
    if pessoa['nome'] == 'Maria':
        print(pessoa['nome'], "mora em", pessoa['cidade'])
        break

# A função range() retorna uma série de números consecutivos. Por padrão, ela inicia no número 0 e é incrementada adicionando 1.
#       range(início, parada, incremento)
# "Escreva um script que imprima os números de 1 até 1000."
for numero in range(10):
    print(numero+1)

# Início e Fim na range()
#       range(inicio, fim)
# "Crie um script em Python que imprima os números de 1 até 5 na tela, usando a função range como elemento de início e o de fim."
for val in range(1,6):
    print(val)  #imprime de 1 a 5



# Início, Fim e o Pulo na range()
#       range(inicio, fim, pulo)

# "Crie um script em Python que imprima os números pares de 1 até 100."
for val in range(2,101,2):
    print(val)

# "Crie um script em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada"
tabuada = int(input('Digite qual tabuada quer saber: '))
for var in range(1,11):
    print(tabuada,'x', var,'=',(tabuada * var))

