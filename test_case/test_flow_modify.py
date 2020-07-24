#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName:test_flow_modify.py
# @Time    :2020/7/22 17:25
# @Author  :Harry
import unittest

from driver.browser import chrome_driver
from page.login_page import LoginPage
from page.user_center_page import UserCenterPage


class ModifyFlowTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = chrome_driver()

    def tearDown(self):
        self.driver.quit()

    def test_modify_flow(self):
        # 登录
        login = LoginPage(self.driver)
        assert_login = login.login("tom", '123456')
        # 修改
        ucp = UserCenterPage(self.driver)
        result = ucp.edit_profile('1987', '6', '8', '18911223344')
        self.assertIn("成功", result)
        self.assertEqual('tom', assert_login)


if __name__ == '__main__':
    unittest.main()