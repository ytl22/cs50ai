import unittest

from tictactoe import actions
X = "X"
O = "O"
EMPTY = None

class TestActions(unittest.TestCase):

	def test_actions(self):
		self.assertEqual(
		actions([[EMPTY, EMPTY, EMPTY],
        		[EMPTY, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY]]), 
		{(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)})
		self.assertEqual(
		actions([[O, EMPTY, EMPTY],
        		[X, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY]]), 
		{(0,1), (0,2), (1,1), (1,2), (2,0), (2,1), (2,2)})
		self.assertEqual(
		actions([[X, EMPTY, EMPTY],
        		[EMPTY, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY]]),
		{(0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)})
		self.assertEqual(
		actions([[X, X, X],
        		[O, O, O],
            	[O, X, X]]), 1, "Should be 1")
		
if __name__ == "__main__":
	unittest.main()