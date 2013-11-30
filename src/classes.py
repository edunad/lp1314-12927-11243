# -*- coding: utf-8 -*-

class District(object):
	def __init__(self, ID=None, INDEX=0):
		self.ID = ID
		self.Count = 0.0
		self.INDEX = INDEX
		
	def __str__(self):
		return str(self.ID) + "->" + str(self.Count)
		
	def __repr__(self):
		return str(self.ID) + "->" + str(self.Count)
		
class Instituicao(object):
	def __init__(self, ID=None, Data=None):
		self.ID = ID
		self.Data = Data
		self.Dist = None
		
	def __str__(self):
		return str(self.ID) + "->" + str(self.Data) + "->" + str(self.Dist)
		
	def __repr__(self):
		return str(self.ID) + "->" + str(self.Data) + "->" + str(self.Dist)
