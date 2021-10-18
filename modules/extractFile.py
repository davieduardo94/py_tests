import zipfile

# nome dos arquivos
fileName = 'nome_do_arquivo.zip'
# local onde está o arquivo
fileIn = 'C:\Temp\CSV\\'
def extractFile():
	print('Extraindo arquivo')
	Zip_ref = zipfile.ZipFile(fileIn+fileName, 'r')
# 	extraindo arquivo para pasta
	Zip_ref.extractall(fileIn)
# 	finalçizando o zipFile
	Zip_ref.close()
