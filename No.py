class No(object):
	"""docstring for ClassName"""
	def __init__(self, identificador):
		super(No, self).__init__()
		self.identificador = identificador

	def __str__(self):
		return '['+self.identificador.__str__()+']'

	def str(self):
		return '['+self.identificador.__str__()+']'
		
		
class NoValorado(No):
	"""docstring for NoValued"""
	def __init__(self, identificador, valor):
		No.__init__(self, identificador)
		self.valor = valor
	def __str__(self):
		return '['+self.identificador.__str__()+'] {'+self.valor.__str__()+'}'

	def str(self):
		return '['+self.identificador.__str__()+'] {'+self.valor.__str__()+'}'