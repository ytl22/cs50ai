import unittest

from tictactoe import player
X = "X"
O = "O"
EMPTY = None
class TestPlayer(unittest.TestCase):
	
	def test_player(self):
		self.assertEqual(
		player([[EMPTY, EMPTY, EMPTY],
        		[EMPTY, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY]]), X, "Should be X")
		self.assertEqual(
		player([[O, EMPTY, EMPTY],
        		[X, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY]]), X, "Should be X")
		self.assertEqual(
		player([[X, EMPTY, EMPTY],
        		[EMPTY, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY]]), O, "Should be O")
		self.assertEqual(
		player([[X, X, X],
        		[O, O, O],
            	[O, X, X]]), 1, "Should be 1")

if __name__ == "__main__":
	unittest.main()
	