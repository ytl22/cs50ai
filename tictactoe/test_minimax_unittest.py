import unittest

from tictactoe import actions, result, player, winner, minimax, minimax_value
X = "X"
O = "O"
EMPTY = None

class TestResult(unittest.TestCase):

	def test_X_win(self):
		self.assertEqual(minimax([[X, X, X],
        		[EMPTY, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY]]),
				None)

	def test_O_win(self):
		self.assertEqual(minimax([[X, O, EMPTY],
        		[O, O, EMPTY],
            	[X, O, EMPTY]]),
				None)

	def test_minmax_value(self):
		self.assertEqual(minimax_value(
				[[X, O, EMPTY],
        		[O, X, EMPTY],
            	[X, O, EMPTY]]),
				1)

	def test_minmax_value2(self):
		self.assertEqual(minimax_value(
				[[X, O, X],
        		[O, O, X],
            	[X, EMPTY, EMPTY]]),
				-1)
	
	def test_minimax(self):
		self.assertEqual(minimax([
				[O, X, X],
        		[X, O, EMPTY],
            	[X, O, EMPTY]]),
				(2,2))

	def test_minimax(self):
		self.assertEqual(minimax([
				[EMPTY, EMPTY, EMPTY],
        		[X, O, EMPTY],
            	[X, O, EMPTY]]),
				(0,0))



if __name__ == "__main__":
	unittest.main()