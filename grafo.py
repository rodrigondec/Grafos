import types
import Queue
import copy
from no import No, NoValorado, NoArvore, NoArvoreDist
from aresta import Aresta, ArestaValorada
from arvore import Arvore, ArvoreDist
from situacao import Situacao

class Grafo(object):

	@classmethod
	def teste(cls):
		print 'teste'

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

	def getAresta(self, origem, destino):
		if origem > destino:
			origem, destino = destino, origem
		elif origem == destino:
			return Situacao(False, "Identificadores iguais do 2 nos")
		for aresta in self.arestas:
			if aresta.origem == origem and aresta.destino == destino:
				return aresta
		return False

	def getAdj(self, identificador):
		adj = []
		for aresta in self.arestas:
			if aresta.origem == identificador:
				adj.append(aresta.destino)
			elif aresta.destino == identificador:
				adj.append(aresta.origem)
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
			if self.getNo(aresta.origem) and self.getNo(aresta.destino):
				if aresta.origem > aresta.destino:
					aresta.origem, aresta.destino = aresta.destino, aresta.origem
				elif aresta.origem == aresta.destino:
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.getAresta(aresta.origem, aresta.destino):
					return Situacao(False, "Aresta ja existe")
				self.arestas.append(aresta)
				return Situacao(True, "Aresta inserida com sucesso")
			return Situacao(False, "1 ou 2 dos Nos n existem")
		return Situacao(False, "Argumento n eh do tipo Aresta")

	def atingivel(self, origem, destino):
		dados = self.dfs(origem)

		if dados['cores'][destino] == 'black':
			return True
		
		return False;

	def caminho(self, origem, destino):
		dados = self.bfs(origem)
		if dados['cores'][destino] == 'black':
			caminho = []
		
			no = dados['arvore'].getNo(destino)
			while 1:
				caminho.append(no.identificador)
				if no.identificador == origem:
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
				# print cores
				for adj in adjs:
					if adj == pais[no]:
						continue
					if cores[adj] == 'white':
						fila.put(adj)
						pais[adj] = no
						cores[adj] = 'gray'
					elif cores[adj] == 'gray':
						return True
		return False

	def num_componentes(self):
		cores = {}
		pais = {}
		for no in self.nos:
			cores[no.identificador] = 'white'
			pais[no.identificador] = None
		num_componentes = 0
		while self.selecionar_brancos(cores):
			num_componentes += 1
			fila = Queue.Queue()
			fila.put(self.selecionar_brancos(cores)[0])

			cores[self.selecionar_brancos(cores)[0]] = 'gray'
			
			while not fila.empty():
				no = fila.get()
				adjs = self.getAdj(no)
				# print 'No: '+no.__str__()
				# print 'adjs: '+adjs.__str__()
				for adj in adjs:
					if cores[adj] == 'white':
						fila.put(adj)
						pais[adj] = no
						cores[adj] = 'gray'
		return num_componentes

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
			if self.getNo(aresta.origem) and self.getNo(aresta.destino):
				if aresta.origem > aresta.destino:
					aresta.origem, aresta.destino = aresta.destino, aresta.origem
				elif aresta.origem == aresta.destino:
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.getAresta(aresta.origem, aresta.destino):
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
			if self.getNo(aresta.origem) and self.getNo(aresta.destino):
				if aresta.origem > aresta.destino:
					aresta.origem, aresta.destino = aresta.destino, aresta.origem
				elif aresta.origem == aresta.destino:
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.getAresta(aresta.origem, aresta.destino):
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
			if aresta.origem == identificador:
				adj.append(aresta.destino)
		return adj

	def getAresta(self, origem, destino):
		if origem == destino:
			return Situacao(False, "Identificadores iguais do 2 nos")
		for aresta in self.arestas:
			if aresta.origem == origem and aresta.destino == destino:
				return True
		return False

	def getSsabagaca(self, identificador):
		for aresta in self.arestas:
			if aresta.origem == identificador or aresta.destino == identificador:
				return aresta
		return False

	def insertAresta(self, aresta):
		if type(aresta) == Aresta:
			if self.getNo(aresta.origem) and self.getNo(aresta.destino):
				if aresta.origem == aresta.destino:
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.getAresta(aresta.origem, aresta.destino):
					return Situacao(False, "Aresta ja existe")
				self.arestas.append(aresta)
				return Situacao(True, "Aresta inserida com sucesso")
			return Situacao(False, "1 ou 2 dos Nos n existem")
		return Situacao(False, "Argumento n eh do tipo Aresta")

	def grau_in(self, identificador):
		grau = 0
		for aresta in self.arestas:
			if aresta.destino == identificador:
				grau += 1
		return grau

	def grau_out(self, identificador):
		grau = 0
		for aresta in self.arestas:
			if aresta.origem == identificador:
				grau += 1
		return grau

	def del_no(self, identificador):
		no = self.getNo(identificador)
		self.nos.remove(no)
		while self.getSsabagaca(identificador):
			self.arestas.remove(self.getSsabagaca(identificador))

	def ord_topol(self):
		if self.ciclico():
			return Situacao(False, "O grafo eh ciclico")
		ordem = []

		grafo = copy.deepcopy(self)

		fila = Queue.Queue()
		for no in grafo.nos:
			if grafo.grau_in(no.identificador) == 0:
				fila.put(no.identificador)
				ordem.append(no.identificador)

		while not fila.empty():
			u = fila.get()
			grafo.del_no(u)

			for no in grafo.nos:
				if not no.identificador in ordem and grafo.grau_in(no.identificador) == 0:
					fila.put(no.identificador)
					ordem.append(no.identificador)

		return ordem

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
			if self.getNo(aresta.origem) and self.getNo(aresta.destino):
				if aresta.origem == aresta.destino:
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.getAresta(aresta.origem, aresta.destino):
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
			if self.getNo(aresta.origem) and self.getNo(aresta.destino):
				if aresta.origem == aresta.destino:
					return Situacao(False, "Identificadores iguais dos 2 Nos")
				if self.getAresta(aresta.origem, aresta.destino):
					return Situacao(False, "Aresta ja existe")
				self.arestas.append(aresta)
				return Situacao(True, "Aresta inserida com sucesso")
			return Situacao(False, "1 ou 2 dos Nos n existem")
		return Situacao(False, "Argumento n eh do tipo ArestaValorada")