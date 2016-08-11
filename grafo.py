import types
import Queue
from No import No, NoValorado, NoArvore
from Aresta import Aresta, ArestaValorada
from Arvore import Arvore
from Situacao import Situacao

class Grafo(object):

	def __init__(self):
		super(Grafo, self).__init__()
		self.nos = []
		self.arestas = []
		self.arvores = {}
		self.arvores['bfs'] = {}
		self.arvores['dfs'] = {}

	def existsNo(self, identificador):
		for no in self.nos:
			if no.identificador == identificador:
				return True
		return False

	def existsAresta(self, identificador1, identificador2):
		if identificador1 > identificador2:
			identificador1, identificador2 = identificador2, identificador1
		elif identificador1 == identificador2:
			return Situacao(False, "Identificadores iguais do 2 nos")
		for aresta in self.arestas:
			if aresta.identificador1 == identificador1 and aresta.identificador2 == identificador2:
				return True
		return False

	def insertNo(self, no):
		if type(no) == No:
			if self.existsNo(no.identificador):
				return Situacao(False, "No ja existe")
			self.nos.append(no)
			return Situacao(True, "No inserido com sucesso")
		return Situacao(False, "Argumento n eh do tipo No")

	def insertAresta(self, aresta):
		if type(aresta) == Aresta:
			if self.existsNo(aresta.identificador1) and self.existsNo(aresta.identificador2):
				if aresta.identificador1 > aresta.identificador2:
					aresta.identificador1, aresta.identificador2 = aresta.identificador2, aresta.identificador1
				elif aresta.identificador1 == aresta.identificador2:
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.existsAresta(aresta.identificador1, aresta.identificador2):
					return Situacao(False, "Aresta ja existe")
				self.arestas.append(aresta)
				return Situacao(True, "Aresta inserida com sucesso")
			return Situacao(False, "1 ou 2 dos Nos n existem")
		return Situacao(False, "Argumento n eh do tipo Aresta")

	def printNos(self):
		for no in self.nos:
			print no

	def printArestas(self):
		for aresta in self.arestas:
			print aresta

	def __str__(self):
		string =  "( "
		if len(self.nos) >= 1:
			string += self.nos[0].str()
		for no in self.nos[1:]:
			string += ", " + no.str()
		string += ";\n"
		if len(self.arestas) >= 1:
			string += self.arestas[0].str()
		for aresta in self.arestas[1:]:
			string += ", " + aresta.str()
		string += " )"
		return string


class Grafo_NoValorado(Grafo):
	"""docstring for Grafo_NoValorado"""
	def __init__(self):
		Grafo.__init__(self)

	def insertNo(self, no):
		if type(no) == NoValorado:
			if self.existsNo(no.identificador):
				return Situacao(False, "No ja existe")
			self.nos.append(no)
			return Situacao(True, "No inserido com sucesso")
		return Situacao(False, "Argumento n eh do tipo NoValorado")
	

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
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.existsAresta(aresta.identificador1, aresta.identificador2):
					return Situacao(False, "Aresta ja existe")
				self.arestas.append(aresta)
				return Situacao(True, "Aresta inserida com sucesso")
			return Situacao(False, "1 ou 2 dos Nos n existem")
		return Situacao(False, "Argumento n eh do tipo ArestaValorada")


class Grafo_Aresta_e_NoValorados(Grafo):
	"""docstring for Grafo_NoEArestaValorados"""
	def __init__(self):
		Grafo.__init__(self)

	def insertNo(self, no):
		if type(no) == NoValorado:
			if self.existsNo(no.identificador):
				return Situacao(False, "No ja existe")
			self.nos.append(no)
			return Situacao(True, "No inserido com sucesso")
		return Situacao(False, "Argumento n eh do tipo NoValorado")

	def insertAresta(self, aresta):
		if type(aresta) == ArestaValorada:
			if self.existsNo(aresta.identificador1) and self.existsNo(aresta.identificador2):
				if aresta.identificador1 > aresta.identificador2:
					aresta.identificador1, aresta.identificador2 = aresta.identificador2, aresta.identificador1
				elif aresta.identificador1 == aresta.identificador2:
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.existsAresta(aresta.identificador1, aresta.identificador2):
					return Situacao(False, "Aresta ja existe")
				self.arestas.append(aresta)
				return Situacao(True, "Aresta inserida com sucesso")
			return Situacao(False, "1 ou 2 dos Nos n existem")
		return Situacao(False, "Argumento n eh do tipo ArestaValorada")
	

class DiGrafo(Grafo):
	"""docstring for DiGrafo"""
	def __init__(self):
		Grafo.__init__(self)

	def existsAresta(self, identificador1, identificador2):
		if identificador1 == identificador2:
			return Situacao(False, "Identificadores iguais do 2 nos")
		for aresta in self.arestas:
			if aresta.identificador1 == identificador1 and aresta.identificador2 == identificador2:
				return True
		return False

	def insertAresta(self, aresta):
		if type(aresta) == Aresta:
			if self.existsNo(aresta.identificador1) and self.existsNo(aresta.identificador2):
				if aresta.identificador1 == aresta.identificador2:
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.existsAresta(aresta.identificador1, aresta.identificador2):
					return Situacao(False, "Aresta ja existe")
				self.arestas.append(aresta)
				return Situacao(True, "Aresta inserida com sucesso")
			return Situacao(False, "1 ou 2 dos Nos n existem")
		return Situacao(False, "Argumento n eh do tipo Aresta")
	

class DiGrafo_NoValorado(DiGrafo):
	"""docstring for ClassName"""
	def __init__(self):
		DiGrafo.__init__(self)

	def insertNo(self, no):
		if type(no) == NoValorado:
			if self.existsNo(no.identificador):
				return Situacao(False, "No ja existe")
			self.nos.append(no)
			return Situacao(True, "No inserido com sucesso")
		return Situacao(False, "Argumento n eh do tipo NoValorado")
	

class DiGrafo_ArestaValorada(DiGrafo):
	"""docstring for ClassName"""
	def __init__(self):
		DiGrafo.__init__(self)

	def insertAresta(self, aresta):
		if type(aresta) == ArestaValorada:
			if self.existsNo(aresta.identificador1) and self.existsNo(aresta.identificador2):
				if aresta.identificador1 == aresta.identificador2:
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.existsAresta(aresta.identificador1, aresta.identificador2):
					return Situacao(False, "Aresta ja existe")
				self.arestas.append(aresta)
				return Situacao(True, "Aresta inserida com sucesso")
			return Situacao(False, "1 ou 2 dos Nos n existem")
		return Situacao(False, "Argumento n eh do tipo ArestaValorada")


class DiGrafo_Aresta_e_NoValorados(DiGrafo):
	def __init__(self):
		DiGrafo.__init__(self)

	def insertNo(self, no):
		if type(no) == NoValorado:
			if self.existsNo(no.identificador):
				return Situacao(False, "No ja existe")
			self.nos.append(no)
			return Situacao(True, "No inserido com sucesso")
		return Situacao(False, "Argumento n eh do tipo NoValorado")

	def insertAresta(self, aresta):
		if type(aresta) == ArestaValorada:
			if self.existsNo(aresta.identificador1) and self.existsNo(aresta.identificador2):
				if aresta.identificador1 == aresta.identificador2:
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.existsAresta(aresta.identificador1, aresta.identificador2):
					return Situacao(False, "Aresta ja existe")
				self.arestas.append(aresta)
				return Situacao(True, "Aresta inserida com sucesso")
			return Situacao(False, "1 ou 2 dos Nos n existem")
		return Situacao(False, "Argumento n eh do tipo ArestaValorada")


grafo = DiGrafo_Aresta_e_NoValorados()

grafo.insertNo(NoValorado(1, 10))

grafo.insertNo(NoValorado(2, 20))

grafo.insertAresta(ArestaValorada(2, 1, 15))

grafo.insertAresta(ArestaValorada(1, 2, 30))

print grafo