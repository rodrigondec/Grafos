from grafo import Grafo
from no import No
from aresta import Aresta
import unittest

class TestStringMethods(unittest.TestCase):
	def setUp(self):
		self.grafo = Grafo()

	def test_upper(self):
		self.grafo.insertNo(No(1))
		self.grafo.insertNo(No(2))
		self.grafo.insertNo(No(3))
		self.grafo.insertNo(No(4))
		self.grafo.insertNo(No(5))
		self.grafo.insertNo(No(6))

		self.assertEqual(len(self.grafo.nos), 6)

		self.grafo.insertAresta(Aresta(1, 2))
		self.grafo.insertAresta(Aresta(1, 5))
		self.grafo.insertAresta(Aresta(5, 2))
		self.grafo.insertAresta(Aresta(5, 4))
		self.grafo.insertAresta(Aresta(2, 3))
		self.grafo.insertAresta(Aresta(3, 4))
		self.grafo.insertAresta(Aresta(4, 6))

		self.assertEqual(len(self.grafo.arestas), 7)

		print self.grafo.bfs(1)

if __name__ == '__main__':
	unittest.main()