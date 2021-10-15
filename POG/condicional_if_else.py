#  ELSE (e indentado) teremos um outro código, que só será executado se a condição testada for FALSE.
# Veja a estrutura de uma teste condicional IF ELSE:
# if True:
    # [codigo]    # Se a condição for verdadeira
    # [codigo]    # o codigo indentado abaixo do if
    # [codigo]    # será executado
# else:
    # [codigo]    # Este bloco de código só funciona
    # [codigo]    # se a condição for falsa

##########   Podemos criar um IF sem um ELSE, mas não existe ELSE sem IF      ##################

print('Time 1: Flamengo')
print('Time 2: Vasco')
time = int(input('Qual o melhor? '))

## if else aninhados
if time==1:
    print('Com certeza esse é o melhor time do mundo, uma vez Flamengo, sempre Flamengo!')
else:
    if time==2:
        print('Vice Vasco')
    else:
        print('Não torce para nenhum desses')



