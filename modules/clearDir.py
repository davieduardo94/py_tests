import os
# funcao para limpar o diretorio
def clearDir():
	print('Limpando diretorio destino')
	destination = 'C:\Temp\CSV\\'
	fileName = 'nome_do_arquivo.extensao'
	os.remove(destination+fileName)
