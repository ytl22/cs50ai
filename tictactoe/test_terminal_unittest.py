import unittest

from tictactoe import actions, result, player, winner, terminal
X = "X"
O = "O"
EMPTY = None

class TestResult(unittest.TestCase):

	def test_termianl(self):
		
		self.assertEqual(terminal([[EMPTY, EMPTY, EMPTY],
        		[EMPTY, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY]]),
				False)
	def test_X_win(self):
		self.assertEqual(terminal([[X, X, X],
        		[EMPTY, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY]]),
				True)

	def test_O_win(self):
		self.assertEqual(terminal([[X, O, EMPTY],
        		[O, O, EMPTY],
            	[X, O, EMPTY]]),
				True)

	def test_O_diag(self):
		self.assertEqual(terminal([
				[O, X, EMPTY],
        		[X, O, EMPTY],
            	[X, O, O]]),
				True)

	def test_filled(self):
		self.assertEqual(terminal([
				[O, X, O],
        		[X, X, O],
            	[X, O, X]]),
				True)	


if __name__ == "__main__":
	unittest.main()