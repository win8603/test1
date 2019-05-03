import unittest , time
from HTMLTestRunner import HTMLTestRunner
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def new_report(testreport):
	lists = os.listdir(testreport)
	lists.sort(key = lambda fn: os.path.getmtime(testreport+"\\"+fn))
	file_new = os.path.join(testreport,lists[-1])
	print(file_new)
	return file_new


def send_mail(file_new):
	f = open(file_new,'rb')
	mail_body = f.read()
	f.close()
	smtpserver = 'smtp.126.com'
	user = 'ouyang8603@126.com'
	password = 'ouyang8603'
	sender = 'ouyang8603@126.com'
	receiver = '297553770@qq.com'
	subject = 'Python email test'
	msg = MIMEText(mail_body,'html','utf-8')
	msg['Subject'] = Header("自动化测试报告",'utf-8')
	msg['FROM'] = 'ouyang8603@126.com'
	msg['TO'] = '297553770@qq.com'
	smtp = smtplib.SMTP()
	smtp.connect(smtpserver)
	smtp.login(user,password)
	smtp.sendmail(sender, receiver, msg.as_string())
	smtp.quit()
	print('emial has send out!')

if __name__ == '__main__':
	test_dir = "./test"
	test_report = "C:\\Users\\Administrator\\Desktop\\TEST\\report"
	discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'test_*.py')
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = test_report + '\\' + now + 'result.html'
	fp = open(filename,'wb')
	runner = HTMLTestRunner(stream = fp ,
		                    title = '百度搜索测试报告',
		                    description = '用例执行情况:')
	runner.run(discover)
	fp.close()	    

	new_report = new_report(test_report)
	send_mail(new_report)  