# Você foi contratado pela Caixa Econômica Federal para atualizar seu sistema.
# Como primeira tarefa, você vai criar um script que diga quanto cada ganhador da Mega-Sena vai receber, ao ter o prêmio dividido com outros ganhadores.
premio = float(input('Valor total do premio: '))
ganhadores = int(input('Quantidade de ganhadores: '))
print('Cada ganhador irá receber R$ %.2f' %(premio/ganhadores))
print('O premio total foi R$%.2f para %d ganhadores, onde cada um ficou \
com R$%.2f' %(premio,ganhadores,premio/ganhadores))
