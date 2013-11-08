# -*- coding: utf-8 -*-

import sqlite3
from classes import *

def get_data(data, where, Command, offset):
	
	MySqlData = []
	TEMPO = []
	
	if type(data) != str or type(Command) != sqlite3.Cursor:
		return None

	Command.execute('SELECT * FROM cna131')
	TempData = Command.fetchall()

	for tmp in TempData:
		
		OffCmnd = tmp[offset].encode('utf-8')
		Command.execute("SELECT " + data + " from cna131 WHERE " + where + "='" + OffCmnd + "'")
		
		if not OffCmnd in TEMPO:
			MySqlData.append(Instituicao(OffCmnd,Command.fetchall()))
			TEMPO.append(OffCmnd)
		
	return MySqlData

#######
def dist_data():
	
	District = []
	District.append('Açores')
	District.append('Algarve')
	District.append('Aveiro')
	District.append('Beira Interior')
	District.append('Coimbra')
	District.append('Évora')
	District.append('Lisboa')
	District.append('Minho')
	District.append('Porto')
	District.append('Trás-os-Montes e Alto Douro')
	District.append('Madeira')
	District.append('Beja')
	District.append('Cávado e do Ave')
	District.append('Bragança')
	District.append('Castelo Branco')
	District.append('Guarda')
	District.append('Leiria')
	District.append('Portalegre')
	District.append('Santarém')
	District.append('Setúbal')
	District.append('Viana do Castelo')
	District.append('Viseu')
	District.append('Tomar')
	District.append('Estoril')
	
	return District
#######

def get_inst(data,Command):
	
	#0 = ID, 1 = List
	Inst_Data = get_data(data,'COD_INST',Command,0)

	ALUN_DIST = []
	Count = 0.0
	
	for tmp in Inst_Data:
		Count = 0
		
		for Inst in tmp.Data:
			Count += Inst[0]
		
		ALUN_DIST.append(Instituicao(tmp.ID,Count))
			
	return ALUN_DIST

def get_dist(data,Command):
	
	#0 = ID, 1 = List
	Inst_Data = get_data(data,'NOME_INST',Command,2)
	print Inst_Data	
	return Inst_Data
	
	
	
	
	
	
	
	
	
	
	
	
	
