'''from my friends copy i don't konw where it come from ==>>如侵删'''


import os
import smtplib
import time
import unittest
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from test_runner.html_test_runner import HTMLTestRunner

'''
整个程序的执行过程分为三步：
1、通过unittest框架的discover()找到匹配测试用例，由HTMLTestRunner的run()方法
执行测试用例并生成最新的测试报告
2、调用new_report()函数找到测试报告目录（Reports）下最新生成的测试报告，返回测试报告的路径
3、将得到的最新测试报告的完整路径传给send_mail()函数，实现发邮件功能
'''



# 查找测试报告目录，找到最新生成的测试报告文件

def new_report(testreport):

    # 获取测试报告目录下的所有文件及文件夹
    lists = os.listdir(testreport)

    # 重新按时间对目录下的文件进行排序
    lists.sort(key=lambda fn:os.path.getmtime(testreport + "\\" + fn))

    # List[-1]取到的就是最新生成的文件或文件夹
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new


# 定义发送邮件

def send_mail(file_new):

    f = open(file_new,'rb')
    mail_body = f.read()

    # 带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，所以，
    # 可以构造一个MIMEMultipart对象代表邮件本身，
    # 然后往里面加上一个MIMEText作为邮件正文，
    # 再继续往里面加上表示附件的MIMEBase对象
    # email模块的MIMEText（）方法用来定义邮件正文，参数为html格式的文本

    # 邮件对象
    msg = MIMEMultipart()

    # email模块的MIMEText（）方法用来定义邮件正文，参数为html格式的文本
    msg.attach(MIMEText(mail_body, 'html', 'utf-8'))

    # email模块的Header（）方法用来定义邮件标题
    msg['Subject'] = Header("自动化测试报告",'utf-8')

    msg['From'] = ""
    msg['To'] = ""

    # 邮件正文是MIMEText
    msg.attach(MIMEText(mail_body, 'html', 'utf-8'))

    # 添加附件就是加上一个MIMEBase,从本地读取测试报告
    mime = MIMEBase('text', 'html', filename=file_new)
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename=file_new)
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来
    mime.set_payload(mail_body)

    # 用Base64编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)

    f.close()

# 修改：1、邮箱地址，对应端口；登录邮箱和授权码（登录qq邮箱-设置-账户-pop3/smtp开启，获取授权码）；
#         发送邮箱和接收邮箱
#      2、指定测试用例目录；指定测试报告目录
#      3、定义测试报告

    smtp = smtplib.SMTP_SSL("smtp.qq.com",465)#邮箱登录方式
    smtp.set_debuglevel(1)
    smtp.login("email@qq.com", "password")#邮箱授权码登录
    smtp.sendmail("email@qq.com", "email@163.com", msg.as_string())#发送邮箱1，接受邮箱2
    smtp.quit()
    print('email has send out !')




if __name__ == '__main__':

    # 指定测试用例目录
    test_dir_login = r'C:\Users\THINK\PycharmProjects\TestProject\Test'


    # 指定测试报告目录
    test_report_login = r'C:\Users\THINK\PycharmProjects\TestProject\reports'

    discover_login = unittest.defaultTestLoader.discover(test_dir_login, pattern='test*.py')



    # 按照一定格式获得当前时间
    now = time.strftime("%Y-%m-%d_%H_%M_%S")

    # 定义报告存放路径
    filename_login = test_report_login + '\\' + now + 'result.html'


    # 以读的方式打开报告文件
    fp_login = open(filename_login, 'wb')


    # 定义测试报告，stream指定测试报告文件，file定义测试报告标题，description定义测试报告副标题
    runner_login = HTMLTestRunner(stream=fp_login,
                               title='广发银行测试报告',
                               description='用例执行情况：')

    runner_login.run(discover_login)  # 运行测试用例

    fp_login.close()  # 关闭报告文件

    new_report_login = new_report(test_report_login)
    send_mail(new_report_login)



