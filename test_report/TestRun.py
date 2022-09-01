import smtplib
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(file_name):
    sender_host = "smtp.163.com"             # 发送方主机地址 为163邮箱

    sender = "xxxxxxx@163.com"               # 需要替换成发送人邮箱
    sender_password = "ASDJASDASDS"          # 需要将STMP服务打开 替换成发送方的一串密码

    receiver = "xxxxxxxxx@qq.com"

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = "邮箱登录系统的Web自动化测试"

    with open(file_name, 'rb') as fp:
        attach = MIMEText( fp.read(), 'base64', 'utf-8')
        attach["Content-Type"]="application/octet-stream"
        attach["Content-Disposition"] = 'attachment;filename="report.html"'

        message.attach(attach)

    smtp = smtplib.SMTP()
    smtp.connect(sender_host)
    smtp.login(sender, sender_password)
    smtp.sendmail(sender, receiver, message.as_string())
    smtp.quit()


suite = unittest.TestLoader().discover('../test_case', 'TestCase.py')

nowtime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
file = '../test_report/' + nowtime +'report.html'                 # 测试报告文件名

with open(file, 'wb') as f:  # 'wb'二进制打开文件不用加encoding
    runner = HTMLTestRunner(f, verbosity=2, title="邮箱登录测试报告", description="Python 3")

    runner.run(suite)  # 必须缩进才能运行，放外面文件关闭就运行不了了

send_email(file)

# stream = sys.stdout 测试报告的文件对象(open) 要是有 wb 打开
# verbosity=1  报告的详细程度， 1 简略  2 详细
# title=None  测试报告标题 可选
# description=None   报告描述信息 可选

