import unittest

from shopping import *

class test(unittest.TestCase):
	def test_load_data(self):
		self.assertEqual(load_data("shopping.csv"), None)


if __name__ == "__main__":
	unittest.main()