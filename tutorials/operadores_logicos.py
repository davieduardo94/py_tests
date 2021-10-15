# Operador AND em Python
# Só vai retornar verdadeiro se TODAS as condições forem verdadeiras!s

idade = int(input('Digite sua idade: '))
if idade>=18 and idade<65:
    print('Você tem que votar')
else:
    print('TA suave')

# Operador OR em Python
# Basta que uma dessas condições seja verdadeira, para o teste condicional ser verdadeiro.
# Para fazermos isso, devemos usar o operador or (ou em português), cujo modelos é o seguinte:

# if condição1 or condição2 or condição3 or ... :
#    [código]   # Caso qualquer condição seja verdadeira
#    [código]   # Esse código vai ser executado
# else:

#    [código]   # Caso todas as condições sejam falsas
#    [código]   # esse código vai ser executado

print('1 - Idoso')
print('2 - gestante')
print('3 - cadeirante')
print('4 - nenhum')

situacao = int(input('Qual a situação: '))
if situacao==1 or situacao==2 or situacao==3:
    print('Você é prioritario')
else:
    print('Voce nao tem prioridade!')

# Operador NOT em Python
# Ele ele pega a expressão e reverte ela.
# Se era uma condição TRUE, ela vira FALSE.
# Se algo era FALSE, ela vira TRUE.

