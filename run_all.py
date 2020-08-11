#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:run_all.py
# @Time    :2020/7/22 15:14
# @Author  :Harry
'''批量执行用例生成报告'''
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

# 批量执行用例
from lib.mail_lib import send_mail
from lib.path_lib import REPORT_PATH, CASE_PATH

print(CASE_PATH)
discover = unittest.defaultTestLoader.discover(start_dir=CASE_PATH,
                                               pattern="test*.py",
                                               top_level_dir=None)
time_str = time.strftime("%Y%m%d%H%M%S", time.localtime())

report_name = REPORT_PATH + '/reoprt-' + time_str + '.html'
title = "ECShop自动化测试"
print(report_name)
with open(report_name, 'wb+') as f:
    runner = HTMLTestRunner(stream=f,
                            title=title,
                            description="自动化测试报告详情")
    runner.run(discover)
# 发送邮件报告
#
send_mail(mail_title=title, mail_body=report_name, mail_type='html')
