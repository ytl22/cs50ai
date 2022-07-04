import unittest

from parser1 import *

class test(unittest.TestCase):

	def test_preprocessed(self):
		self.assertEqual(preprocess("Good muffins cost $3.88\nin New York.  Please buy me\
... two of them.\n\nThanks."), None)


if __name__ == "__main__":
	unittest.main()