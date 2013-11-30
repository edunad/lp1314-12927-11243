# -*- coding: utf-8 -*-

import xlrd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

from classes import *
from xlrd import open_workbook

Connection = sqlite3.connect('cna131fresultados.db')
Command = Connection.cursor()

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

def implementDistrict(data,DistData):
	TEMPDATA = data
	
	for tmp in TEMPDATA:
		
		IN = isInList(tmp.ID,DistData)		
		tmp.Dist = District(DistData[IN].ID,IN)
	
	return TEMPDATA

def isInList(stri,data):
	
	for indx in range(len(data)) :
		if stri.find(data[indx].ID) != -1:
			return indx
			
	return indx
		
	
#######
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

def get_dist_per(data):
	Dt = get_dist(data)
	
	for tmp in Dt:
		tmp.Count /= 1000

	return Dt
	
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
	
	
	
def create_graph_inst(data, title, y_title,x_title):
	
	Values = []
	IDS = []
	
	fig = plt.figure()
	ax = plt.subplot(111)
	width = 20

	for tmp in data:
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

def create_graph_dist(data, title, y_title,x_title):
	
	Values = []
	IDS = []
	
	fig = plt.figure()
	ax = plt.subplot(111)
	width = 20

	for tmp in data:
		Values.append(tmp.Count)
		IDS.append(tmp.ID.decode('utf-8'))
		
	Size = np.arange(len(IDS)) * width
	ax.bar(Size, Values, width = width)
	
	ax.set_xticks(Size + width/2)
	ax.set_xticklabels(IDS, rotation=90)
	ax.set_xlabel(x_title)
	ax.set_ylabel(y_title)
	ax.set_title(title)
	
	plt.grid(True)
	plt.show()
	
	
	
	
	
	
	
