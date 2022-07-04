import unittest

from tictactoe import actions, result, player, winner, utility
X = "X"
O = "O"
EMPTY = None

class TestResult(unittest.TestCase):

	def test_X_win(self):
		self.assertEqual(utility([[X, X, X],
        		[EMPTY, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY]]),
				1)

	def test_O_win(self):
		self.assertEqual(utility([[X, O, EMPTY],
        		[O, O, EMPTY],
            	[X, O, EMPTY]]),
				-1)

	def test_O_diag(self):
		self.assertEqual(utility([
				[O, X, EMPTY],
        		[X, O, EMPTY],
            	[X, O, O]]),
				-1)

	def test_filled(self):
		self.assertEqual(utility([
				[O, X, O],
        		[X, X, O],
            	[X, O, X]]),
				0)	


if __name__ == "__main__":
	unittest.main()