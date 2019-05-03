#encoding = 'utf-8'
from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from test1 import Count

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
	#testunit.addTest(Baidu("test_add"))
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = './' + now + 'result.html'
	fp = open(filename,'wb')
	runner = HTMLTestRunner(stream = fp ,
		                    title = '百度搜索测试报告',
		                    description = '用例执行情况:')
	runner.run(suite)
	fp.close()	                    		

