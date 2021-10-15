import csv
import pandas
import data
import pyodbc
# abrindo arquivo
caminho='\\\\192.168.200.220\\Canvas\\blue_integration\\Data\\Pres\\zip\\'
salvar='\\\\192.168.200.220\\Canvas\\blue_integration\\Data\\Pres\\'
cnxn 	= 	pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+data.serverAddress+';DATABASE='+data.database+';UID='+data.dbUser+';PWD='+data.dbPassword)
crsr  	= 	cnxn.cursor()
# with open(caminho+'courses.csv', encoding='utf-8') as arquivo:

# ler tabela
	# tabela = csv.reader(arquivo)
	# #navegar pela tabela
	# for text in arquivo:
    # 		print(text)

arqcsv = open(caminho+'courses.csv', mode='r', encoding='utf-8', newline='',)
# ler = csv.reader(arqcsv)
# for text in ler:
# 	text = text.rstrip('\n')
# 	print('insert into courses_prod values (',text,')')
# arqcsv.close()

# for [course_id, short_name, long_name] in ler:
def odbcExec(sql):
	crsr.execute(sql)
	cnxn.commit()

def closeODBC():
	crsr.close()
	cnxn.close()

# conexao
def conectSQL():
	cnxn =pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+data.serverAddress+';DATABASE='+data.database+';UID='+data.dbUser+';PWD='+data.dbPassword)
	crsr =cnxn.cursor()

csv_arq = ''.join([i for i in arqcsv]).replace(',',',')
replac = open(salvar+"course_replace.csv",mode="w",encoding="utf-8")
replac.writelines(csv_arq)
replac.close()

#  funcao para importar os dados do CSV para o banco
def importData():
	# abrindo o arquivo na pasta
	with open(salvar+'courses.csv', mode='r', encoding='utf-8', newline='') as csv_file:
		# fazendo a leitura
		csv_reader = csv.reader(csv_file, delimiter=',')
		# ignorando o cabecalho csv
		csv_reader.__next__()
		# concatenando comando SQL
		for row in csv_reader:
			sql="""insert into courses_prod(course_id, short_name, long_name, account_id, term_id, status, course_format, blueprint_course_id) values (""""'"+row[0]+"','"+row[2]+"','"+row[3]+"','"+row[4]+"','"+row[5]+"','"+row[6]+"','"+row[9]+"','"+row[10]+"')"""
			print(sql)
			# conectando ao banco
			conectSQL()
			# executando SQL
			odbcExec(sql)
		# fechando conexao
		closeODBC()

importData()






	