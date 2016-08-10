import types
from No import No, NoValorado
from Aresta import Aresta, ArestaValorada
from Situacao import Situacao

class Grafo(object):

	def __init__(self):
		super(Grafo, self).__init__()
		self.nos = []
		self.arestas = []

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

	def printNos(self):
		for no in self.nos:
			print no

	def printArestas(self):
		for aresta in self.arestas:
			print aresta

	def __str__(self):
		string =  "("
		if len(self.nos) >= 1:
			string += self.nos[0].str()
		for no in self.nos[1:]:
			string += ", " + no.str()
		string += ";\n"
		if len(self.arestas) >= 1:
			string += self.arestas[0].str()
		for aresta in self.arestas[1:]:
			string += ", " + aresta.str()
		string += ")"
		return string


class Grafo_NoValorado(Grafo):
	"""docstring for Grafo_NoValorado"""
	def __init__(self):
		Grafo.__init__(self)

	def insertNo(self, no):
		if type(no) == NoValorado:
			if self.existsNo(no.identificador):
				return Situacao(False, "Nodulo ja existe")
			self.nos.append(no)
			return Situacao(True, "Nodulo inserido com sucesso")
		return Situacao(False, "Argumento n eh do tipo Nodulo Valorado")
	

class Grafo_ArestaValorada(Grafo):
	"""docstring for Grafo_ArestaValorada"""
	def __init__(self):
		Grafo.__init__(self)
		
	def insertAresta(self, aresta):
		if type(aresta) == ArestaValorada:
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
		return Situacao(False, "Argumento n eh do tipo Aresta Valorada")


class Grafo_Aresta_e_NoValorados(Grafo):
	"""docstring for Grafo_NoEArestaValorados"""
	def __init__(self):
		Grafo.__init__(self)

	def insertNo(self, no):
		if type(no) == NoValorado:
			if self.existsNo(no.identificador):
				return Situacao(False, "Nodulo ja existe")
			self.nos.append(no)
			return Situacao(True, "Nodulo inserido com sucesso")
		return Situacao(False, "Argumento n eh do tipo Nodulo Valorado")

	def insertAresta(self, aresta):
		if type(aresta) == ArestaValorada:
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
		return Situacao(False, "Argumento n eh do tipo Aresta Valorada")
	

class DiGrafo(Grafo):
	"""docstring for DiGrafo"""
	def __init__(self):
		Grafo.__init__(self)

	def existsAresta(self, identificador1, identificador2):
		if identificador1 == identificador2:
			return Situacao(False, "Identificadores iguais do 2 nodulos")
		for aresta in self.arestas:
			if aresta.identificador1 == identificador1 and aresta.identificador2 == identificador2:
				return True
		return False

	def insertAresta(self, aresta):
		if type(aresta) == Aresta:
			if self.existsNo(aresta.identificador1) and self.existsNo(aresta.identificador2):
				if aresta.identificador1 == aresta.identificador2:
					return Situacao(False, "Identificadores iguais dos 2 nodulos")
				if self.existsAresta(aresta.identificador1, aresta.identificador2):
					return Situacao(False, "Aresta ja existe")
				self.arestas.append(aresta)
				return Situacao(True, "Aresta inserida com sucesso")
			return Situacao(False, "1 ou 2 dos nodulos n existem")
		return Situacao(False, "Argumento n eh do tipo Aresta")
	

class DiGrafo_NoValorado(DiGrafo):
	"""docstring for ClassName"""
	def __init__(self):
		DiGrafo.__init__(self)

	def insertNo(self, no):
		if type(no) == NoValorado:
			if self.existsNo(no.identificador):
				return Situacao(False, "Nodulo ja existe")
			self.nos.append(no)
			return Situacao(True, "Nodulo inserido com sucesso")
		return Situacao(False, "Argumento n eh do tipo Nodulo Valorado")
		



grafo = DiGrafo_NoValorado()

grafo.insertNo(NoValorado(1, 15))

print grafo.insertNo(NoValorado(2, 30))

grafo.insertAresta(Aresta(2, 1))

grafo.insertAresta(Aresta(1, 2))

print grafo