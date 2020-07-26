import unittest

from driver.browser import chrome_driver
from page.login_page import LoginPage


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = chrome_driver()
    def test_login_a(self):
        '''合法登录'''
        lp = LoginPage(self.driver)
        actual = lp.login('tom', "123456")
        self.assertEqual('tom', actual)

if __name__ == '__main__':
    unittest.main()
