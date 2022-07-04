import unittest

from tictactoe import actions, result, player, winner
X = "X"
O = "O"
EMPTY = None

class TestResult(unittest.TestCase):

	def test_winner(self):
		
		self.assertEqual(winner([[EMPTY, EMPTY, EMPTY],
        		[EMPTY, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY]]),
				None)
	def test_X_win(self):
		self.assertEqual(winner([[X, X, X],
        		[EMPTY, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY]]),
				X)

	def test_O_win(self):
		self.assertEqual(winner([[X, O, EMPTY],
        		[O, O, EMPTY],
            	[X, O, EMPTY]]),
				O)
	def test_O_diag(self):
		self.assertEqual(winner([
				[O, X, EMPTY],
        		[X, O, EMPTY],
            	[X, O, O]]),
				O)

if __name__ == "__main__":
	unittest.main()