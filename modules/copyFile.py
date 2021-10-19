import shutil
import os
import glob

def copyFile():
	print('Copiando arquivo para pasta de log')
#   caminho onde está o arquivo
	fileFolder = 'C:\Temp\CSV\\'
	# buscando apenas os arquivos com o nome especifico na pasta
	fileToCopy = glob.glob(os.path.join(fileFolder,'nome_arquivo*.zip'))
#   executando a copia para pasta criada
	for fileInFolder in fileToCopy:
			shutil.copy(fileInFolder,fileFolder+'\\log\\')		
