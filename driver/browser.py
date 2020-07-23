#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:browser.py
# @Time    :2020/7/22 10:46
# @Author  :Harry
from selenium import webdriver
'''封装浏览器驱动'''
def chrome_driver():
    '''Chrome 浏览器'''
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver

def firefox_deiver():
    '''Firefox浏览器'''
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver