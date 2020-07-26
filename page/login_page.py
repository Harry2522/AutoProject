#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:login_page.py
# @Time    :2020/7/22 10:35
# @Author  :Harry
import time

from selenium.webdriver.common.by import By

from lib.path_lib import BASE_URL
from page.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self,driver):
        self.url = BASE_URL

        self.driver= driver
        #元素定位符
        self.locator_username = (By.NAME, 'username')  #用户名输入框
        self.locator_password = (By.NAME, 'password') #密码输入框
        self.locator_submit = (By.NAME, 'submit')  #登录按钮
        self.locator_assert = (By.XPATH, '//font[@id="ECS_MEMBERZONE"]/a[1]') #断言定位符

    def ele_username(self,username): #用户名定位及操作
        # self.driver.find_element(*self.locator_username).send_keys(username)
        self.find_element(self.locator_username).send_keys(username)

    def ele_password(self, passwd): #密码的定位及操作
        # self.driver.find_element(*self.locator_password).send_keys(passwd)
        self.find_element(self.locator_password).send_keys(passwd)

    def ele_submit(self):  #登录按钮的定位及操作
        # self.driver.find_element(*self.locator_submit).click()
        self.find_element(self.locator_submit).click()

    def login(self, username, passwd):
        '''登录逻辑'''
        self.open(self.url)
        self.ele_username(username)
        self.ele_password(passwd)
        self.ele_submit()
        time.sleep(2)
        actual_result = self.assert_result(self.locator_assert)
        # self.quit()
        return actual_result

