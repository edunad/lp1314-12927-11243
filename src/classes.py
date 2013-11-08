# -*- coding: utf-8 -*-

class Instituicao(object):
	def __init__(self, ID=None, Data=None):
		self.ID = ID
		self.Data = Data
		
	def __str__(self):
		return str(self.ID) + "->" + str(self.Data)
		
	def __repr__(self):
		return str(self.ID) + "->" + str(self.Data)
