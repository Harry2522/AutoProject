#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:path_lib.py
# @Time    :2020/7/25 16:08
# @Author  :Harry
import os

BASE_URL = 'http://437.webjsw.com/'
# BASE_URL = "http://192.168.1.241/hdshop/"
BASE_PATH = os.path.dirname(os.getcwd())
CASE_PATH = os.path.join(BASE_PATH, 'test_case')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
DATA_PATH = os.path.join(BASE_PATH, 'data')

