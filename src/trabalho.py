# -*- coding: utf-8 -*-
# autor: 12927 11243
# data: 23 de Outubro de 2013

import xlrd
import sqlite3
from classes import *
from functions import *
from xlrd import open_workbook

ficheiro = open_workbook('cna131fresultados.xls')

RawData = []
FinalData = []
Count = 0
CountInsert = 0

# Leitura do EXCEL

for s in ficheiro.sheets():
	for row in range(s.nrows):
		if Count > 2:
			for col in range(s.ncols):	
				 
				 if CountInsert > 8:
					 FinalData.append(RawData)
					 RawData = []
					 CountInsert = 0
				 		 
				 RawData.append(s.cell_value(row,col))
				 CountInsert += 1
				 
		Count+=1


# Ligação a base de dados

Connection = sqlite3.connect('cna131fresultados.db')
Command = Connection.cursor()

# Criaçao da TABELA
Command.execute('DROP TABLE IF EXISTS cna131')
Command.execute('CREATE TABLE cna131 (COD_INST text, COD_CUR text, NOME_INST text, NOME_CURS text, GRAU text, VAGA_INIC float, COLOC float, NOTA float, VAGA_SOBR float)')
Connection.commit()

for indx in range(len(FinalData) - 1):
	#print 'Index = ', indx ,' -> ', FinalData[indx] 
	Command.execute('INSERT INTO cna131 VALUES(?,?,?,?,?,?,?,?,?)',FinalData[indx])

Connection.commit()

########################
## Obter Estatisticas ##


# Aluno por Inst
#print get_inst('COLOC',Command)

# Vagas
#print get_inst('VAGA_SOBR',Command)

# Aluno por Distrito
get_dist('COLOC',Command)




