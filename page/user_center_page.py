#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:user_center_page.py
# @Time    :2020/7/22 17:54
# @Author  :Harry
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class UserCenterPage(BasePage):
    def __init__(self, driver):
        self.driver= driver
        #导航菜单
        self.loc_nav_user_profile=(By.LINK_TEXT,"用户信息")
        self.loc_nav_order_list=(By.LINK_TEXT, "我的订单")
        self.loc_nav_address_list =(By.LINK_TEXT, "收货地址")
        #用户信息
        self.loc_select_year =(By.NAME,'birthdayYear')
        self.loc_select_month = (By.NAME, 'birthdayMonth')
        self.loc_select_day = (By.NAME, 'birthdayDay')
        self.loc_assert = (By.XPATH,'/html/body/div[6]/div/div/div/div/p[1]')
        self.loc_ele_mobile=(By.NAME, 'extend_field5')
        self.loc_ele_modify_submit=(By.XPATH,'//form[@name="formEdit"]/table/tbody/tr[10]/td/input[2]')
    def nav_user_profile(self):
        self.driver.find_element(*self.loc_nav_user_profile).click()

    def nav_order_list(self):
        self.driver.find_element(*self.loc_nav_order_list).click()

    def nav_address_list(self):
        self.driver.find_element(*self.loc_nav_address_list).click()

    def ele_prof_birth(self,year,month,day):
        self.select(self.loc_select_year, year)
        self.select(self.loc_select_month, month)
        self.select(self.loc_select_day, day)

    def ele_mobile(self,mobile):
        self.driver.find_element(*self.loc_ele_mobile).clear()
        self.driver.find_element(*self.loc_ele_mobile).send_keys(mobile)

    def ele_modify_submit(self):
        self.driver.find_element(*self.loc_ele_modify_submit).click()

    def edit_profile(self,year,month,day,mobile):
        self.nav_user_profile()
        self.ele_prof_birth(year=year,month=month,day=day)
        self.ele_mobile(mobile=mobile)
        self.ele_modify_submit()
        result = self.assert_result(self.loc_assert)
        return result