# -*- coding: utf-8 -*-

import xlrd
import sqlite3
from classes import *
from xlrd import open_workbook

def get_data(data, where, Command, offset, filt):
	
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
def dist_data():
	
	Districts = []
	
	Districts.append(District('Açores'))
	Districts.append(District('Algarve'))
	Districts.append(District('Aveiro'))
	Districts.append(District('Beira Interior'))
	Districts.append(District('Coimbra'))
	Districts.append(District('Évora'))
	Districts.append(District('Lisboa'))
	Districts.append(District('Minho'))
	Districts.append(District('Porto'))
	Districts.append(District('Trás-os-Montes e Alto Douro'))
	Districts.append(District('Madeira'))
	Districts.append(District('Beja'))
	Districts.append(District('Cávado e do Ave'))
	Districts.append(District('Bragança'))
	Districts.append(District('Castelo Branco'))
	Districts.append(District('Guarda'))
	Districts.append(District('Leiria'))
	Districts.append(District('Portalegre'))
	Districts.append(District('Santarém'))
	Districts.append(District('Setúbal'))
	Districts.append(District('Viana do Castelo'))
	Districts.append(District('Viseu'))
	Districts.append(District('Tomar'))
	Districts.append(District('Estoril'))
	
	Districts.append(District('Unknown'))
	
	return Districts
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
def get_inst(data,Command):
	
	#0 = ID, 1 = List
	Inst_Data = get_data(data,'COD_INST',Command,0,'')

	ALUN_DIST = []
	
	for tmp in Inst_Data:
		Count = 0
		
		for Inst in tmp.Data:
			Count += Inst[0]
		
		ALUN_DIST.append(Instituicao(tmp.ID,Count))
			
	return ALUN_DIST

def get_dist(data,Command):
	
	Districts = dist_data()
	#0 = ID, 1 = List
	Data = implementDistrict(get_data(data,'NOME_INST',Command,2,''),Districts)
	
	for temp in Data:
		Count = 0
		
		for inst in temp.Data:
			Count += inst[0]
		
		Indx = temp.Dist.INDEX
		Districts[Indx].Count += Count
	
	
	return Districts

def get_dist_per(data,Command):
	Dt = get_dist(data,Command)
	
	for tmp in Dt:
		tmp.Count /= 1000

	return Dt
	
def get_total_perc(Command):
	Alunos = get_inst('COLOC',Command)
	TOTAL = 0.0
	
	for tmp in Alunos:
		TOTAL += tmp.Data
		
	for tmp in Alunos:
		tmp.Data /= TOTAL
		tmp.Data *= 100
		tmp.Data = round(tmp.Data,4)
	
	return Alunos
	
	
	
	
	
	
	
	
	
	
	
