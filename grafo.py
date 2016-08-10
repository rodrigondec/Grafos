import types
from No import No
from Aresta import Aresta


class Grafo(object):

	def __init__(self):
		super(Grafo, self).__init__()
		self.nos = []
		self.arestas = []

	def insertNo(self, no):
		if type(no) == No:
			self.nos.append(no)

	def insertAresta(self, aresta):
		if type(aresta) == Aresta and existsNo(aresta.identificador1) and existsNo(aresta.identificador2):
			self.arestas.append(aresta)

	def existsNo(self, identificador):
		for no in self.nos:
			if no.identificador == identificador:
				return True
		return False

	def existsAresta(self, identificador1, identificador2):
		if identificador1 > identificador2:
			identificador1, identificador2 = identificador2, identificador1
		elif identificador1 == identificador2:
			print "IDENTIFICADORES IGUAIS"
			return False
		for aresta in self.arestas:
			if aresta.identificador1 == identificador1 and aresta.identificador2 == identificador2:
				return True
		return False


grafo = Grafo()

grafo.insertNo(No(1))

print grafo.existsNo(2)