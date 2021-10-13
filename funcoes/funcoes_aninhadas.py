# Função chamando Função - Tutorial de Python
#  funções 'conversam' entre si, uma chama a outra, elas podem e devem trabalhar juntas!

def mensagem():
    print("O melhor curso de todos é:")
    python_progressivo()
    print("Estude por lá!")

def python_progressivo():
    print("Curso Python Progressivo")

mensagem()

# Variável Local em Python
# Se você criou e usou uma variável dentro de qualquer função, ela só existe naquele escopo, ou seja, apenas ali dentro da função.
# Quem está de 'fora', não sabe que ela existe, não sabe o que tem dentro da função.
