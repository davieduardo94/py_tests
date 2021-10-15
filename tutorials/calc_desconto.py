preco = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o % de desconto: '))
calcDesconto = (desconto/100) * preco
totalProduto = (preco-calcDesconto)
print('Valor original: ', preco, '\nValor do Desconto: ',calcDesconto, '\nValor com Desconto: ', totalProduto)
