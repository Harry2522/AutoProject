#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:base_page.py
# @Time    :2020/7/22 16:43
# @Author  :Harry
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class BasePage():
    '''公共page'''
    def __init__(self,driver):
        # self.driver = chrome_driver()
        self.driver = driver

    def assert_result(self,locator_assert):
        '''断言处理'''
        actual_result = self.driver.find_element(*locator_assert).text
        return actual_result

    def open(self,url):
        self.driver.get(url=url)

    def find_element(self,locator):
        return self.driver.find_element(*locator)

    def find_element_a(self, by_type, loc):
        if by_type == 'id':
            ele = self.driver.find_element(By.ID, loc)
        elif by_type == 'name':
            ele = self.driver.find_element(By.NAME, loc)
        elif by_type == 'tag':
            ele = self.driver.find_element(By.TAG_NAME, loc)
        elif by_type == 'xpath':
            ele = self.driver.find_element(By.XPATH, loc)
        elif by_type == 'link':
            ele = self.driver.find_element(By.LINK_TEXT, loc)
        elif by_type == 'class':
            ele = self.driver.find_element(By.CLASS_NAME, loc)
        elif by_type == "css":
            ele = self.driver.find_element(By.CSS_SELECTOR, loc)
        else:
            ele = self.driver.find_element(By.PARTIAL_LINK_TEXT, loc)
        return ele

    def quit(self):
        self.driver.quit()

    def select(self,select_loctor,select_values):
        sel_ele = self.driver.find_element(*select_loctor)
        select = Select(sel_ele)
        select.select_by_value(select_values)
        time.sleep(1)
