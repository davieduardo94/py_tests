import zipfile

# caminho onde vai salvar para presencial
sourcePres = 'C:\Temp\Pres\\'
# caminho onde vai salvar para ead
sourceEAD = 'C:\Temp\EAD\\'
# pasta onde será baixado o arquivo csv
downFile = 'C:\Temp\CSV\\'
# nome dos arquivos
fileEAD = 'EAD.zip'
filePres = 'Pres.zip'

def extractFile(account):
	if(account==215):
		fileName = filePres
		fileIn = sourcePres
	else:
		fileName = fileEAD
		fileIn = sourceEAD
	print('Extraindo arquivo')
	Zip_ref = zipfile.ZipFile(fileIn+fileName, 'r')
	Zip_ref.extractall(fileIn)
	Zip_ref.close()
