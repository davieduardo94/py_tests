import shutil
import os

# caminho onde vai salvar os arquivos
destination = 'C:\Temp\\'
# pasta onde será baixado o arquivo csv
downloadFile = 'C:\Temp\CSV\\'

def moveFile(account):
	print('Movendo arquivo para pasta selecionada')
# 	listando arquivos no diretorio
	dataDir = os.listdir(downloadFile)	
	for fileInFolder in dataDir:
		shutil.move(downloadFile+fileInFolder,destination)
