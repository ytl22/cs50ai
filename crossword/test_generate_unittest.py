import unittest

from generate import *
from crossword import *

structure = "data/structure0.txt"
words = "data/words0.txt"
crossword = Crossword(structure, words)
creator = CrosswordCreator(crossword)

class test(unittest.TestCase):

	def test_simple(self):
		self.assertEqual(creator.enforce_node_consistency(), None)

	def test_revise(self):
		var = [v for v in crossword.variables]
		self.assertEqual(creator.revise(var[0], var[1]), None)

	def test_ac3(self):
		self.assertEqual(creator.ac3(), None)

	
if __name__ == "__main__":
	unittest.main()