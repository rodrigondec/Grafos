import types
from No import No
from Aresta import Aresta
from Situacao import Situacao

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
			return Situacao(False, "Identificadores iguais do 2 nodulos")
		for aresta in self.arestas:
			if aresta.identificador1 == identificador1 and aresta.identificador2 == identificador2:
				return True
		return False

	def insertNo(self, no):
		if type(no) == No:
			if self.existsNo(no.identificador):
				return Situacao(False, "Nodulo ja existe")
			self.nos.append(no)
			return Situacao(True, "Nodulo inserido com sucesso")
		return Situacao(False, "Argumento n eh do tipo Nodulo")

	def insertAresta(self, aresta):
		if type(aresta) == Aresta:
			if self.existsNo(aresta.identificador1) and self.existsNo(aresta.identificador2):
				if aresta.identificador1 > aresta.identificador2:
					aresta.identificador1, aresta.identificador2 = aresta.identificador2, aresta.identificador1
				elif aresta.identificador1 == aresta.identificador2:
					return Situacao(False, "Identificadores iguais dos 2 nodulos")
				if self.existsAresta(aresta.identificador1, aresta.identificador2):
					return Situacao(False, "Aresta ja existe")
				self.arestas.append(aresta)
				return Situacao(True, "Aresta inserida com sucesso")
			return Situacao(False, "1 ou 2 dos nodulos n existem")
		return Situacao(False, "Argumento n eh do tipo Aresta")
grafo = Grafo()

grafo.insertNo(No(1))

print grafo.existsNo(2)