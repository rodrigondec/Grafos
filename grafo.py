import types
import Queue
from no import No, NoValorado, NoArvore, NoArvoreDist
from aresta import Aresta, ArestaValorada
from arvore import Arvore, ArvoreDist
from situacao import Situacao

class Grafo(object):

	def __init__(self):
		super(Grafo, self).__init__()
		self.nos = []
		self.arestas = []
		self.arvores = {}

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

	def atingivel(self, identificador1, identificador2):
		dados = self.dfs(identificador1)

		if dados['cores'][identificador2] == 'black':
			return True
		
		return False;

	def caminho(self, identificador1, identificador2):
		dados = self.bfs(identificador1)
		if dados['cores'][identificador2] == 'black':
			caminho = []
		
			no = dados['arvore'].getNo(identificador2)
			while 1:
				caminho.append(no.identificador)
				if no.identificador == identificador1:
					break
				no = dados['arvore'].getNo(no.pai)
			caminho.reverse()
			return caminho
		return False

	def conexo(self):
		dados = self.bfs(self.nos[0].identificador)
		for cor in dados['cores']:
			if dados['cores'][cor] == 'white':
				return False
		return True

	def selecionar_brancos(self, cores):
		brancos = []
		for key in cores:
			if cores[key] == 'white':
				brancos.append(key)
		return brancos

	def ciclico(self):
		cores = {}
		pais = {}
		for no in self.nos:
			cores[no.identificador] = 'white'
			pais[no.identificador] = None

		while self.selecionar_brancos(cores):

			fila = Queue.Queue()
			fila.put(self.selecionar_brancos(cores)[0])

			cores[self.selecionar_brancos(cores)[0]] = 'gray'
			
			while not fila.empty():
				no = fila.get()
				adjs = self.getAdj(no)
				# print 'No: '+no.__str__()
				# print 'adjs: '+adjs.__str__()
				for adj in adjs:
					if adj == pais[no]:
						continue
					if cores[adj] == 'white':
						fila.put(adj)
						pais[adj] = no
						cores[adj] = 'gray'
					elif cores[adj] == 'gray':
						# print cores
						return True
		return False

	def bfs(self, identificador):
		if not self.getNo(identificador):
			return Situacao(False, "No n existe no grafo")

		arvore = ArvoreDist(self.getNo(identificador))
		distancias = {}
		pais = {}
		cores = {}
		for no in self.nos:
			cores[no.identificador] = 'white'
			distancias[no.identificador] = 0
			pais[no.identificador] = None

		cores[identificador] = 'gray'
	
		fila = Queue.Queue()
		fila.put(identificador)

		while not fila.empty():
			u = fila.get()
			adjs = self.getAdj(u)
			for adj in adjs:
				if cores[adj] == 'white':
					cores[adj] = 'gray'
					distancias[adj] = distancias[u] + 1
					pais[adj] = u
					fila.put(adj)
					arvore.insertNo(NoArvoreDist(adj, pais[adj], distancias[adj]))
			cores[u] = 'black'

		# print cores
		# print pai

		return {'arvore': arvore, 'pais': pais, 'cores': cores, 'distancias': distancias}

	def dfs(self, identificador):
		if not self.getNo(identificador):
			return Situacao(False, "No n existe no grafo")

		arvore = Arvore(self.getNo(identificador))
	
		pais = {}
		cores = {}
		for no in self.nos:
			cores[no.identificador] = 'white'
			pais[no.identificador] = None

		pilha = [identificador]
		
		while pilha:
			u = pilha.pop()
			cores[u] = 'gray'
			adjs = self.getAdj(u)
			for adj in adjs:
				if cores[adj] == 'white':
					pais[adj] = u
					pilha.append(adj)
			cores[u] = 'black'

		# print cores
		# print pai
		
		for key in pais:
			if key != identificador:
				arvore.insertNo(NoArvore(key, pais[key]))
		return {'arvore': arvore, 'pais': pais, 'cores': cores}

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

	def getAdj(self, identificador):
		adj = []
		for aresta in self.arestas:
			if aresta.identificador1 == identificador:
				adj.append(aresta.identificador2)
		return adj

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