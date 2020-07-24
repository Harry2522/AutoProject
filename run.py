#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:run.py
# @Time    :2020/7/24 17:06
# @Author  :Harry

import smtplib
import time
import unittest
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from BeautifulReport import BeautifulReport

from lib.user_lib import MAIL_USER, MAIL_PASSWD

# 加载测试用例

discover = unittest.defaultTestLoader.discover(r'D:\workspace\webUIAuto\test_case', 'test*.py')
# 执行测试用例，生成报告
now = time.strftime('%Y%m%d%H%M%S')
filename = "crm_test{}.html".format(now)
BeautifulReport(discover).report(description='crm登录测试',
                                 log_path='report',
                                 filename=filename)
# 发送邮件
filename = "./report/{}".format(filename)
with open(filename, 'rb') as f:
    mail_body = f.read()
text = MIMEText(mail_body, 'html', 'utf-8')

msg = MIMEMultipart()
msg.attach(text)
msg['Subject'] = Header('crm自动化测试报告', 'utf-8')
msg['From'] = MAIL_USER
msg['To'] = 'H<931665795@qq.com>'

# 添加附件
att = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
att['Content-Type'] = "application/octet-stream"
att['Content-Disposition'] = 'attachment;filename={}'.format(filename)
msg.attach(att)

smtp = smtplib.SMTP('smtp.163.com')
smtp.login(MAIL_USER, MAIL_PASSWD)
smtp.sendmail(msg['From'], msg['To'], msg.as_string())
smtp.quit()
print("邮件发送完成")
