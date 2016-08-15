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

class NoArvore(No):
	def __init__(self, identificador, pai):
		No.__init__(self, identificador)
		self.pai = pai

	def __str__(self):
		return '['+self.identificador.__str__()+'] {'+self.pai.__str__()+'}'

	def str(self):
		return '['+self.identificador.__str__()+'] {'+self.pai.__str__()+'}'


class NoArvoreDist(NoArvore):
	def __init__(self, identificador, pai, distancia):
		NoArvore.__init__(self, identificador, pai)
		self.distancia = distancia

	def __str__(self):
		return '['+self.identificador.__str__()+'] {'+self.pai.__str__()+'} ('+self.distancia.__str__()+')'

	def str(self):
		return '['+self.identificador.__str__()+'] {'+self.pai.__str__()+'} ('+self.distancia.__str__()+')'
