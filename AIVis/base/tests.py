from django.test import TestCase
from base.src.algorithms import *

# Create your tests here
class SearchTestCase(TestCase):
	graph = {'a': ['b', 'c'], 'b': ['d', 'e'], 'c': ['f', 'g']} 
	def setUp(self):
		pass

	def test_bfs(self):
		result = bfs.bfs(self.graph, 'a')
		self.assertListEqual(result, ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
	
	def test_dfs(self):
		result = dfs.dfs(self.graph, 'a')
		self.assertListEqual(result, ['a','b','d','e','c','f','g'])