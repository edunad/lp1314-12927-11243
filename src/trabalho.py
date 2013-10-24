# -*- coding: utf-8 -*-
# autor: 12927 11243
# data: 23 de Outubro de 2013

import xlrd
import sqlite3

from xlrd import open_workbook

ficheiro = open_workbook('cna131fresultados.xls')

RawData = []
Data = []
Count = 0

# Leitura do EXCEL

for s in ficheiro.sheets():
	for row in range(s.nrows):
		if Count > 2:
			for col in range(s.ncols):	
				RawData.append(unicode(str(s.cell(row,col)),'utf-8'))
				
		Count+=1

# Inserção de dados na base de dados

FinalData = []
DataTemp = []

Count = 0

for index in range(len(RawData)):
	
	temp = str(RawData[index]).split(':')
	st = temp[1].replace("'",'') # retirar as pelicas
	
	if temp[0] == 'text':
		st = st[1:] # retirar o 'u'
		
	if temp[0] == 'number':
		st = float(st) # converter para float
		
	if Count > 8:
		FinalData.append(DataTemp)
		DataTemp = []
		Count = 0
		
	DataTemp.append(st)	
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

## TESTE ##
Command.execute('SELECT * FROM cna131')
data = Command.fetchall()

for tm in data:
	print tm

Connection.close()
