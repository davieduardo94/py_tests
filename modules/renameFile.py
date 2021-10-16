import os

fileIn = 'C:\Temp\\'
newFile ='novo_arquivo.zip'

def renameFile():
#   verificar os arquivos no diretorio
	dataDir = os.listdir(fileIn)
#   validando se esta vazio
	if(dataDir==[]):
		print('Pasta vazia')
	else:
		print('Arquivos na pasta: ', dataDir)
#     aqui ira renomear o arquivo na pasta para novo nome
#  PROBLEMA: se houver mais de 1 arquivo ocorrerá Exception
		for fileInFolder in dataDir:
			print(os.rename(fileIn+fileInFolder, fileIn+newFile))
