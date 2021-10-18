import shutil
import os

# caminho onde vai salvar para presencial
sourcePres = 'C:\Temp\Pres\\'
# caminho onde vai salvar para ead
sourceEAD = 'C:\Temp\EAD\\'
# pasta onde será baixado o arquivo csv
downFile = 'C:\Temp\CSV\\'
# nome dos arquivos
fileEAD = 'EAD.zip'
filePres = 'Pres.zip'

def moveFile(account):
	print('Movendo arquivo para pasta selecionada')
	if(account==215):
		destination = sourcePres
	else:
		destination = sourceEAD
	fileIn = downFile
	dataDir = os.listdir(fileIn)	
	for fileInFolder in dataDir:
			shutil.move(fileIn+fileInFolder,destination)
