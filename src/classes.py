
class Instituicao(object):
	def __init__(self, ID=None, Count=None):
		self.ID = ID
		self.Count = Count
		
	def __str__(self):
		return self.ID
		
	def __repr__(self):
		return self.ID + " -> " + str(self.Count)
