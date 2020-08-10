import unittest

import ddt

from driver.browser import chrome_driver
from page.login_page import LoginPage


@ddt.ddt
class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = chrome_driver()

    @ddt.data(('tom', '23456'))
    def test_login_a(self, username, passwd):
        '''合法登录'''
        lp = LoginPage(self.driver)
        actual = lp.login(username, passwd)
        self.assertEqual(username, actual)

if __name__ == '__main__':
    unittest.main()
