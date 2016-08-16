from grafo import Grafo
from no import No
from aresta import Aresta
import unittest

class TestStringMethods(unittest.TestCase):
	def setUp(self):
		self.grafo = Grafo()

	def test_atingivel(self):
		self.grafo.insertNo(No(1))
		self.grafo.insertNo(No(2))
		self.grafo.insertNo(No(3))
		self.grafo.insertNo(No(4))
		self.grafo.insertNo(No(5))
		self.grafo.insertNo(No(6))
		self.grafo.insertNo(No(7))
		self.assertEqual(len(self.grafo.nos), 7)

		self.grafo.insertAresta(Aresta(1, 2))
		self.grafo.insertAresta(Aresta(1, 5))
		self.grafo.insertAresta(Aresta(5, 2))
		self.grafo.insertAresta(Aresta(5, 4))
		self.grafo.insertAresta(Aresta(2, 3))
		self.grafo.insertAresta(Aresta(3, 4))
		self.grafo.insertAresta(Aresta(4, 6))
		self.assertEqual(len(self.grafo.arestas), 7)

		self.assertEqual(self.grafo.atingivel(1, 6), True)

		self.assertEqual(self.grafo.atingivel(1, 7), False)

	def test_caminho(self):
		self.grafo.insertNo(No(1))
		self.grafo.insertNo(No(2))
		self.grafo.insertNo(No(3))
		self.grafo.insertNo(No(4))
		self.grafo.insertNo(No(5))
		self.grafo.insertNo(No(6))
		self.grafo.insertNo(No(7))
		self.assertEqual(len(self.grafo.nos), 7)

		self.grafo.insertAresta(Aresta(1, 2))
		self.grafo.insertAresta(Aresta(1, 5))
		self.grafo.insertAresta(Aresta(5, 2))
		self.grafo.insertAresta(Aresta(5, 4))
		self.grafo.insertAresta(Aresta(2, 3))
		self.grafo.insertAresta(Aresta(3, 4))
		self.grafo.insertAresta(Aresta(4, 6))
		self.assertEqual(len(self.grafo.arestas), 7)

		self.assertEqual(self.grafo.caminho(1, 6), [1, 5, 4, 6])

		self.assertEqual(self.grafo.caminho(1, 3), [1, 2, 3])

	def test_conexo(self):
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

		self.assertEqual(self.grafo.conexo(), True)

		self.grafo.insertNo(No(7))
		self.assertEqual(len(self.grafo.nos), 7)

		self.assertEqual(self.grafo.conexo(), False)

	def test_ciclico_true(self):
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

		self.assertEqual(self.grafo.ciclico(), True)

	def test_ciclico_false(self):
		self.grafo.insertNo(No(1))
		self.grafo.insertNo(No(2))
		self.grafo.insertNo(No(3))
		self.grafo.insertNo(No(4))
		self.grafo.insertNo(No(5))
		self.grafo.insertNo(No(6))
		self.assertEqual(len(self.grafo.nos), 6)

		self.grafo.insertAresta(Aresta(1, 2))
		self.grafo.insertAresta(Aresta(1, 5))
		self.grafo.insertAresta(Aresta(5, 4))
		self.grafo.insertAresta(Aresta(2, 3))
		self.grafo.insertAresta(Aresta(4, 6))
		self.assertEqual(len(self.grafo.arestas), 5)

		self.assertEqual(self.grafo.ciclico(), False)

	def test_ciclico_n_conexo_true(self):
		self.grafo.insertNo(No(1))
		self.grafo.insertNo(No(2))
		self.grafo.insertNo(No(3))
		self.grafo.insertNo(No(4))
		self.grafo.insertNo(No(5))
		self.grafo.insertNo(No(6))
		self.grafo.insertNo(No(7))
		self.grafo.insertNo(No(8))
		self.grafo.insertNo(No(9))
		self.grafo.insertNo(No(10))
		self.assertEqual(len(self.grafo.nos), 10)

		self.grafo.insertAresta(Aresta(1, 2))
		self.grafo.insertAresta(Aresta(1, 5))
		self.grafo.insertAresta(Aresta(5, 4))
		self.grafo.insertAresta(Aresta(2, 3))
		self.grafo.insertAresta(Aresta(7, 6))
		self.grafo.insertAresta(Aresta(8, 9))
		self.grafo.insertAresta(Aresta(9, 10))
		self.grafo.insertAresta(Aresta(8, 10))
		self.assertEqual(len(self.grafo.arestas), 8)

		self.assertEqual(self.grafo.ciclico(), True)

	def test_ciclico_n_conexo_false(self):
		self.grafo.insertNo(No(1))
		self.grafo.insertNo(No(2))
		self.grafo.insertNo(No(3))
		self.grafo.insertNo(No(4))
		self.grafo.insertNo(No(5))
		self.grafo.insertNo(No(6))
		self.grafo.insertNo(No(7))
		self.grafo.insertNo(No(8))
		self.grafo.insertNo(No(9))
		self.grafo.insertNo(No(10))
		self.assertEqual(len(self.grafo.nos), 10)

		self.grafo.insertAresta(Aresta(1, 2))
		self.grafo.insertAresta(Aresta(1, 5))
		self.grafo.insertAresta(Aresta(5, 4))
		self.grafo.insertAresta(Aresta(2, 3))
		self.grafo.insertAresta(Aresta(7, 6))
		self.grafo.insertAresta(Aresta(8, 9))
		self.grafo.insertAresta(Aresta(9, 10))
		self.assertEqual(len(self.grafo.arestas), 7)

		self.assertEqual(self.grafo.ciclico(), False)

	def test_num_componentes(self):
		self.grafo.insertNo(No(1))
		self.grafo.insertNo(No(2))
		self.grafo.insertNo(No(3))
		self.grafo.insertNo(No(4))
		self.grafo.insertNo(No(5))
		self.assertEqual(len(self.grafo.nos), 5)

		self.grafo.insertAresta(Aresta(1, 2))
		self.grafo.insertAresta(Aresta(1, 5))
		self.grafo.insertAresta(Aresta(5, 4))
		self.grafo.insertAresta(Aresta(2, 3))
		self.assertEqual(len(self.grafo.arestas), 4)

		self.assertEqual(self.grafo.num_componentes(), 1)

		self.grafo.insertNo(No(6))
		self.grafo.insertNo(No(7))
		self.assertEqual(len(self.grafo.nos), 7)

		self.grafo.insertAresta(Aresta(7, 6))
		self.assertEqual(len(self.grafo.arestas), 5)

		self.assertEqual(self.grafo.num_componentes(), 2)

		self.grafo.insertNo(No(8))
		self.grafo.insertNo(No(9))
		self.grafo.insertNo(No(10))
		self.assertEqual(len(self.grafo.nos), 10)

		self.grafo.insertAresta(Aresta(8, 9))
		self.grafo.insertAresta(Aresta(9, 10))
		self.grafo.insertAresta(Aresta(8, 10))
		self.assertEqual(len(self.grafo.arestas), 8)

		self.assertEqual(self.grafo.num_componentes(), 3)

	def test_bfs(self):
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

		self.grafo.bfs(1)

	def test_dfs(self):
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

		self.grafo.dfs(1)

if __name__ == '__main__':
	unittest.main()