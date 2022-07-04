import unittest

from traffic import *

class test(unittest.TestCase):
	def test_load_data(self):
		self.assertEqual(load_data("gtsrb_small"), None)

if __name__ == "__main__":
	unittest.main()