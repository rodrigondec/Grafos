import types
import Queue
from no import No, NoValorado, NoArvore
from aresta import Aresta, ArestaValorada
from arvore import Arvore
from situacao import Situacao

class Grafo(object):

	def __init__(self):
		super(Grafo, self).__init__()
		self.nos = []
		self.arestas = []
		self.arvores = {}
		self.arvores['bfs'] = {}
		self.arvores['dfs'] = {}

	def getNo(self, identificador):
		for no in self.nos:
			if no.identificador == identificador:
				return no
		return False

	def getAresta(self, identificador1, identificador2):
		if identificador1 > identificador2:
			identificador1, identificador2 = identificador2, identificador1
		elif identificador1 == identificador2:
			return Situacao(False, "Identificadores iguais do 2 nos")
		for aresta in self.arestas:
			if aresta.identificador1 == identificador1 and aresta.identificador2 == identificador2:
				return aresta
		return False

	def getAdj(self, identificador):
		adj = []
		for aresta in self.arestas:
			if aresta.identificador1 == identificador:
				adj.append(aresta.identificador2)
			elif aresta.identificador2 == identificador:
				adj.append(aresta.identificador1)
		return adj

	def insertNo(self, no):
		if type(no) == No:
			if self.getNo(no.identificador):
				return Situacao(False, "No ja existe")
			self.nos.append(no)
			return Situacao(True, "No inserido com sucesso")
		return Situacao(False, "Argumento n eh do tipo No")

	def insertAresta(self, aresta):
		if type(aresta) == Aresta:
			if self.getNo(aresta.identificador1) and self.getNo(aresta.identificador2):
				if aresta.identificador1 > aresta.identificador2:
					aresta.identificador1, aresta.identificador2 = aresta.identificador2, aresta.identificador1
				elif aresta.identificador1 == aresta.identificador2:
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.getAresta(aresta.identificador1, aresta.identificador2):
					return Situacao(False, "Aresta ja existe")
				self.arestas.append(aresta)
				return Situacao(True, "Aresta inserida com sucesso")
			return Situacao(False, "1 ou 2 dos Nos n existem")
		return Situacao(False, "Argumento n eh do tipo Aresta")

	def bfs(self, identificador):
		if not self.getNo(identificador):
			return Situacao(False, "No n existe no grafo")

		self.arvores['bfs'][identificador] = Arvore(self.getNo(identificador))
	
		distancia = {}
		pai = {}
		color = {}
		for no in self.nos:
			color[no.identificador] = 'white'
			distancia[no.identificador] = 0
			pai[no.identificador] = None

		# print color
		# print distancia
		# print pai

		color[identificador] = 'gray'
	
		fila = Queue.Queue()
		fila.put(identificador)

		while not fila.empty():
			u = fila.get()
			adjs = self.getAdj(u)
			for adj in adjs:
				if color[adj] == 'white':
					color[adj] = 'gray'
					distancia[adj] = distancia[u] + 1
					pai[adj] = u
					fila.put(adj)
					self.arvores['bfs'][identificador].insertNo(NoArvore(adj, pai[adj], distancia[adj]))
			color[u] = 'black'

		return self.arvores['bfs'][identificador]


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
			if self.getNo(no.identificador):
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
			if self.getNo(aresta.identificador1) and self.getNo(aresta.identificador2):
				if aresta.identificador1 > aresta.identificador2:
					aresta.identificador1, aresta.identificador2 = aresta.identificador2, aresta.identificador1
				elif aresta.identificador1 == aresta.identificador2:
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.getAresta(aresta.identificador1, aresta.identificador2):
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
			if self.getNo(no.identificador):
				return Situacao(False, "No ja existe")
			self.nos.append(no)
			return Situacao(True, "No inserido com sucesso")
		return Situacao(False, "Argumento n eh do tipo NoValorado")

	def insertAresta(self, aresta):
		if type(aresta) == ArestaValorada:
			if self.getNo(aresta.identificador1) and self.getNo(aresta.identificador2):
				if aresta.identificador1 > aresta.identificador2:
					aresta.identificador1, aresta.identificador2 = aresta.identificador2, aresta.identificador1
				elif aresta.identificador1 == aresta.identificador2:
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.getAresta(aresta.identificador1, aresta.identificador2):
					return Situacao(False, "Aresta ja existe")
				self.arestas.append(aresta)
				return Situacao(True, "Aresta inserida com sucesso")
			return Situacao(False, "1 ou 2 dos Nos n existem")
		return Situacao(False, "Argumento n eh do tipo ArestaValorada")
	

class DiGrafo(Grafo):
	"""docstring for DiGrafo"""
	def __init__(self):
		Grafo.__init__(self)

	def getAresta(self, identificador1, identificador2):
		if identificador1 == identificador2:
			return Situacao(False, "Identificadores iguais do 2 nos")
		for aresta in self.arestas:
			if aresta.identificador1 == identificador1 and aresta.identificador2 == identificador2:
				return True
		return False

	def insertAresta(self, aresta):
		if type(aresta) == Aresta:
			if self.getNo(aresta.identificador1) and self.getNo(aresta.identificador2):
				if aresta.identificador1 == aresta.identificador2:
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.getAresta(aresta.identificador1, aresta.identificador2):
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
			if self.getNo(no.identificador):
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
			if self.getNo(aresta.identificador1) and self.getNo(aresta.identificador2):
				if aresta.identificador1 == aresta.identificador2:
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.getAresta(aresta.identificador1, aresta.identificador2):
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
			if self.getNo(no.identificador):
				return Situacao(False, "No ja existe")
			self.nos.append(no)
			return Situacao(True, "No inserido com sucesso")
		return Situacao(False, "Argumento n eh do tipo NoValorado")

	def insertAresta(self, aresta):
		if type(aresta) == ArestaValorada:
			if self.getNo(aresta.identificador1) and self.getNo(aresta.identificador2):
				if aresta.identificador1 == aresta.identificador2:
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.getAresta(aresta.identificador1, aresta.identificador2):
					return Situacao(False, "Aresta ja existe")
				self.arestas.append(aresta)
				return Situacao(True, "Aresta inserida com sucesso")
			return Situacao(False, "1 ou 2 dos Nos n existem")
		return Situacao(False, "Argumento n eh do tipo ArestaValorada")


# grafo = DiGrafo()

# grafo.insertNo(No(1))

# grafo.insertNo(No(4))

# grafo.insertNo(No(3))

# grafo.insertAresta(Aresta(4, 1))

# grafo.insertAresta(Aresta(3, 4))

# grafo.bfs(1)

# grafo.bfs(4)

# grafo.bfs(3)

# for arvore in grafo.arvores['bfs']:
# 	print grafo.arvores['bfs'][arvore]
