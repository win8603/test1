from test1 import Count
import unittest

class TestAdd(unittest.TestCase):

	def setUp(self):
		print("test is start")

	def test_add(self):
		j = Count(2,3)
		self.assertEqual(j.add(),5)	

	def test_add2(self):
		j = Count(41,76)
		self.assertEqual(j.add(),117)

	def teatDown(self):
		print("test is over")
		
if __name__ == '__main__':
	suite =	unittest.TestSuite()
	suite.addTest(TestAdd("test_add"))
	suite.addTest(TestAdd("test_add2"))	
	runner = unittest.TextTestRunner()
	runner.run(suite)			