import shutil
import os

# caminho onde vai salvar os arquivos
destination = 'C:\Temp\\'
# pasta onde será baixado o arquivo csv
downloadFile = 'C:\Temp\CSV\\'

def moveFile(fileName,extension):
	print('Movendo arquivo para pasta selecionada')
# 	listando arquivos no diretorio
	dataDir = glob.glob(os.path.join(os.path.expanduser('~'), f'{downloadFile}\\{fileName}*'+extension))
	for fileInFolder in dataDir:
		shutil.move(downloadFile+fileInFolder,destination)
