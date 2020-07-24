import unittest

from driver.browser import chrome_driver
from page.LoginPage import LoginPage
from page.UpdateUserPage import UpdateUserPage


class UpdateUserTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = chrome_driver()  # 初始化driver驱动
        # 调用登录逻辑
        login = LoginPage(self.driver)
        login.login("vivian009", "zhm12345")

    def tearDown(self):
        self.driver.quit()

    def test_update_user(self):
        up = UpdateUserPage(self.driver)  # driver2
        up.update_user()

        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
