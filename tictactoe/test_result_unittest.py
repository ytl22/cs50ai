import unittest

from tictactoe import actions, result, player
X = "X"
O = "O"
EMPTY = None

class TestResult(unittest.TestCase):

	def test_result(self):
		self.assertRaises(Exception, result, [[EMPTY, EMPTY, EMPTY],
        		[EMPTY, X, EMPTY],
            	[EMPTY, EMPTY, EMPTY]],(1,1))
		self.assertEqual(result([[EMPTY, EMPTY, EMPTY],
        		[EMPTY, EMPTY, EMPTY],
            	[EMPTY, EMPTY, EMPTY]], (1,1)),
				[[EMPTY, EMPTY, EMPTY],
        		[EMPTY, X, EMPTY],
            	[EMPTY, EMPTY, EMPTY]])

if __name__ == "__main__":
	unittest.main()