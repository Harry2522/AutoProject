#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:register_page.py
# @Time    :2020/7/22 15:47
# @Author  :Harry
import time
from selenium.webdriver.common.by import By
from driver.browser import chrome_driver
from page.base_page import BasePage

class RegisterPage(BasePage):
    def __init__(self):
        super().__init__()
        # self.driver=chrome_driver()
        self.url = "http://192.168.1.241/hdshop/user.php?act=register"
        self.loc_elem_username = (By.NAME,'username')
        self.loc_elem_email = (By.NAME, 'email')
        self.loc_elem_passwd = (By.NAME, 'password')
        self.loc_elem_confirm_passwd = (By.NAME, 'confirm_password')
        self.loc_elem_mobile = (By.NAME, 'extend_field5')
        self.loc_elem_submit = (By.NAME, 'Submit')
        self.locator_assert= (By.XPATH,'//font[@id="ECS_MEMBERZONE"]/a[1]')

    def elem_username(self,username):
        self.driver.find_element(*self.loc_elem_username).send_keys(username)

    def elem_email(self,email):
        self.driver.find_element(*self.loc_elem_email).send_keys(email)

    def elem_passwd(self,passwd):
        self.driver.find_element(*self.loc_elem_passwd).send_keys(passwd)

    def elem_confirm_passwd(self,confirm_passwd):
        self.driver.find_element(*self.loc_elem_confirm_passwd).send_keys(confirm_passwd)

    def elem_mobile(self,mobile):
        self.driver.find_element(*self.loc_elem_mobile).send_keys(mobile)

    def elem_submit(self):
        self.driver.find_element(*self.loc_elem_submit).click()

    def register(self,username,email,passwd,confirm_passwd,mobile):
        # self.driver.get(url=self.url)
        self.open(self.url)
        self.elem_username(username)
        self.elem_email(email)
        self.elem_passwd(passwd)
        self.elem_confirm_passwd(confirm_passwd)
        self.elem_mobile(mobile)
        self.elem_submit()
        time.sleep(3)
        result = self.assert_result(self.locator_assert)
        self.quit()

        return result


