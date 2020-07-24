#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:mail_lib.py
# @Time    :2020/7/22 23:15
# @Author  :Harry

import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from lib.user_lib import MAIL_USER, MAIL_PASSWD


def post_mail():
    smtp_server = "smtp.l63.com"  # smtp 服务器
    sender = 'Harry<zhr10187@163.com>'  # 发送邮箱
    receiver = 'HR<931665795@qq.com>'  # 接收邮箱

    subject = "Web自动化测试报告"
    mail_body = "<html><head></head><body><h1>hello Email </h1></body</html>"

    # 邮件正文
    text = MIMEText(mail_body, 'html', 'utf-8')
    msg = MIMEMultipart()
    msg.attach(text)
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver
    # msg['To'] = [receiver,sender,'zhr<zhr10187@126.com>','zhang<931665795@qq.com>']

    # 邮件附件
    file_name = r'D:\workspace\webAuto41\report\reoprt-202007201325.html'
    att = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="%s"' % (file_name)
    msg.attach(att)

    # 发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server, 25)
        smtp.login(MAIL_USER, MAIL_PASSWD)
        smtp.sendmail(msg['From'], msg['To'], msg.as_string())
        smtp.quit()
    except Exception as e:
        print("邮件发送失败：", e)
    else:
        print("邮件发送成功")


post_mail()

def send_mail():
    '''发送邮件'''
    # 邮件发送和接收人
    sender = "Harry< %s >" % MAIL_USER
    receiver = "Z<931665795@qq.com>"
    smtpserver = 'smtp.163.com'
    # 登录的用户名密码
    username = MAIL_USER
    password = MAIL_PASSWD
    # 邮件标题
    subject = "CRMWeb自动化测试报告-2020-02"
    mail_type = 'html'  # 邮件发送类型：HTML、text、plain

    # 邮件内容
    filename = r'D:\workspace\webAuto41\report\reoprt-202007201325.html'
    with open(filename, 'r', encoding='utf-8') as f:
        mail_body = f.read()
        msg = MIMEText(mail_body, mail_type, 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    # 添加附件

    # 邮件发送
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("邮件发送成功")

# send_mail()
