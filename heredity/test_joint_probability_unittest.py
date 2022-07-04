import unittest

from heredity import joint_probability, inherit_p
people = {
'Harry': {'name': 'Harry', 'mother': 'Lily', 'father': 'James', 'trait': None},
'James': {'name': 'James', 'mother': None, 'father': None, 'trait': True},
'Lily': {'name': 'Lily', 'mother': None, 'father': None, 'trait': False}
}
one_gene = {"Harry"}
two_gene = {"James"}
have_trait = {"James"}

class TestJointP(unittest.TestCase):
	
	def test_no_parent(self):
		self.assertEqual(joint_probability(people, one_gene, two_gene, have_trait), None)

	def test_inherit_p(self):
		self.assertEqual(inherit_p(2,1), None)
if __name__ == "__main__":
	unittest.main()