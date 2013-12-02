# -*- coding: utf-8 -*-
# autor: 12927 11243
# data: 23 de Outubro de 2013

import xlrd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import csv

from classes import *
from xlrd import open_workbook

Connection = sqlite3.connect('cna131fresultados.db')
Command = Connection.cursor()

# Get data from the database
def get_data(data, where, offset, filt):
	
	MySqlData = []
	TEMPO = []
	
	if type(data) != str or type(Command) != sqlite3.Cursor:
		return None

	Command.execute('SELECT * FROM cna131')
	TempData = Command.fetchall()

	for tmp in TempData:
		
		OffCmnd = tmp[offset].encode('utf-8')
		Command.execute("SELECT " + data + " from cna131 WHERE " + where + "='" + OffCmnd + "'")
		
		if filt != '' :
			OffCmnd = OffCmnd.split(filt)[0]
		
		if not OffCmnd in TEMPO:
			MySqlData.append(Instituicao(OffCmnd,Command.fetchall()))
			TEMPO.append(OffCmnd)
		
	return MySqlData

#######
	
# Read the XLS file containing districts
def get_dist_data():
	District_Data = []
	District_Database = open_workbook('district-database.xls')
	
	for s in District_Database.sheets():
		for row in range(s.nrows):
			for col in range(s.ncols):	
				District_Data.append(District(s.cell_value(row,col).encode('utf-8')))
				
				
	District_Data.append(District('Unknown'))
	return District_Data

#######

# Set the districts to the insts
def implementDistrict(data,DistData):
	TEMPDATA = data
	
	for tmp in TEMPDATA:
		
		IN = isInList(tmp.ID,DistData)		
		tmp.Dist = District(DistData[IN].ID,IN)
	
	return TEMPDATA

# Check if its in the list. If its not, return the last value on the "data" (AKA Unkown)
def isInList(stri,data):
	
	for indx in range(len(data)) :
		if stri.find(data[indx].ID) != -1:
			return indx
			
	return indx
		
	
#######
# Get the Institution
def get_inst(data):
	
	#0 = ID, 1 = List
	Inst_Data = get_data(data,'COD_INST',0,'')

	ALUN_DIST = []
	
	for tmp in Inst_Data:
		Count = 0
		
		for Inst in tmp.Data:
			Count += Inst[0]
		
		ALUN_DIST.append(Instituicao(tmp.ID,Count))
			
	return ALUN_DIST

# Get the District
def get_dist(data):
	
	Districts = get_dist_data()
	#0 = ID, 1 = List
	Data = implementDistrict(get_data(data,'NOME_INST',2,''),Districts)
	
	for temp in Data:
		Count = 0
		
		for inst in temp.Data:
			Count += inst[0]
		
		Indx = temp.Dist.INDEX
		Districts[Indx].Count += Count
	
	
	return Districts

# Permilagem on dist
def get_dist_per(data):
	Dt = get_dist(data)
	
	for tmp in Dt:
		tmp.Count /= 1000

	return Dt
	
# Percent on Inst
def get_total_perc():
	Alunos = get_inst('COLOC')
	TOTAL = 0.0
	
	for tmp in Alunos:
		TOTAL += tmp.Data
		
	for tmp in Alunos:
		tmp.Data /= TOTAL
		tmp.Data *= 100
		tmp.Data = round(tmp.Data,4)
	
	return Alunos
	
# Create the graphics
def create_graph(data, title, y_title,x_title,isDist):
	
	Values = []
	IDS = []
	
	fig = plt.figure()
	ax = plt.subplot(111)
	width = 20

	for tmp in data:
		if isDist :
			Values.append(tmp.Count)
			IDS.append(tmp.ID.decode('utf-8'))
		else:
			Values.append(tmp.Data)
			IDS.append(int(tmp.ID))
		
	Size = np.arange(len(IDS)) * width
	ax.bar(Size, Values, width = width)
	ax.set_xticks(Size + width/2)
	ax.set_xticklabels(IDS, rotation=90)
	ax.set_xlabel(x_title)
	ax.set_ylabel(y_title)
	ax.set_title(title)
	
	plt.grid(True)
	plt.show()
	
def save_statistics():
	with open('statistics.csv','wb')as csvfile:
		writer = csv.writer(csvfile)
		
		# 1º Estatistica
		writer.writerow("==== Alunos Por Instituição ====")
		
		for t in get_inst('COLOC'):
			writer.writerow(str(t))
			
		# 2º Estatistica
		writer.writerow("==== Alunos Por Distrito ====")
		
		for t in get_dist('COLOC'):
			writer.writerow(str(t))
			
		# 3º Estatistica
		writer.writerow("==== Permilagem Alunos por Distrito ====")
		
		for t in get_dist_per('COLOC'):
			writer.writerow(str(t))
			
		# 4º Estatistica
		writer.writerow("==== Percentagem Alunos por Instituiçao ====")
		
		for t in get_total_perc():
			writer.writerow(str(t))
			
		# 5º Estatistica
		writer.writerow("==== Vagas por Colocar por Instituição ====")
		
		for t in get_inst('VAGA_SOBR'):
			writer.writerow(str(t))
			
		# 6º Estatistica
		writer.writerow("==== Vagas por Colocar por Distrito ====")
		
		for t in get_dist('VAGA_SOBR'):
			writer.writerow(str(t))
	
