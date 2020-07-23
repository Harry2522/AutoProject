#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:mail_lib.py
# @Time    :2020/7/22 23:15
# @Author  :Harry

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
from lib.user_lib import MAIL,PASSWD,MAIL_SERVER

def post_mail():
    smtp_server = "smtp.l63.com"
    # user= 'zhr10187@163.com'
    # passwd = 'SMHPQGMZYJCLHXLG' #163邮箱授权码

    sender = 'Harry<zhr10187@163.com>'  #发送邮箱
    receiver = 'HR<931665795@qq.com>' #接收邮箱

    subject = "Web自动化测试报告"
    mail_body = "<html><head></head><body><h1>hello Email </h1></body</html>"

    text = MIMEText(mail_body,'html','utf-8')
    msg = MIMEMultipart()
    msg.attach(text)
    msg['Subject'] = Header(subject,'utf-8')
    msg['From'] = sender
    msg['To'] = 'zhang<931665795@qq.com>'
    # msg['To'] = [receiver,sender,'zhr<zhr10187@126.com>','zhang<931665795@qq.com>']

    #发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtp_server,25)
    smtp.login(MAIL,PASSWD)
    smtp.sendmail(msg['From'],msg['To'], msg.as_string())
    smtp.quit()
    print("邮件发送成功")

# post_mail()

def send_mail():
    '''发送邮件'''
    #
    sender ="Harry< %s >" % MAIL
    receiver = "Z<931665795@qq.com>"
    subject = "CRMWeb自动化测试报告-2020-02"
    mail_type = 'html'
    smtpserver = 'smtp.163.com'
    username = MAIL
    password = PASSWD

    filename = r'D:\workspace\webAuto41\report\reoprt-202007201325.html'
    with open(filename,'r',encoding='utf-8') as f:
        mail_body = f.read()
        # print(mail_body)
        msg = MIMEText(mail_body, mail_type, 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver,25)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("邮件发送成功")

send_mail()