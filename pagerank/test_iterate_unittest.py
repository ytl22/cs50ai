import unittest

from pagerank import iterate_pagerank

class TestIterate(unittest.TestCase):

	def test_1_html(self):
		
		self.assertEqual(iterate_pagerank(
			{"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}},
			0.85),
			{"1.html": 0.05, "2.html": 0.475, "3.html": 0.475})
	'''
	def test_no_outlink(self):
		self.assertEqual(sample_pagerank({"1.html": {}, "2.html": {"3.html"}, "3.html": {"2.html"}},
			"1.html",
			0.85),
			{"1.html": 0.3333, "2.html": 0.3333, "3.html": 0.3333})
	'''
	

if __name__ == "__main__":
	unittest.main()