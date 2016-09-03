class Aresta(object):
	"""docstring for Aresta"""
	def __init__(self, origem, destino):
		super(Aresta, self).__init__()
		self.origem = origem
		self.destino = destino

	def __str__(self):
		return '['+self.origem.__str__()+', '+self.destino.__str__()+']'

	def str(self):
		return '['+self.origem.__str__()+', '+self.destino.__str__()+']'

class ArestaValorada(Aresta):
	"""docstring for ArestaValor"""
	def __init__(self, origem, destino, valor):
		Aresta.__init__(self, origem, destino)
		self.valor = valor
	
	def __str__(self):
		return '['+self.origem.__str__()+', '+self.destino.__str__()+'] {'+self.valor.__str__()+'}'

	def str(self):
		return '['+self.origem.__str__()+', '+self.destino.__str__()+'] {'+self.valor.__str__()+'}'