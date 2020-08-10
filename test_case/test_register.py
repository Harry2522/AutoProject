import unittest
import unittest

import ddt

from driver.browser import chrome_driver
from lib.data_lib import read_csv
from page.register_page import RegisterPage


@ddt.ddt
class RegisterTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = chrome_driver()

    # @ddt.file_data(os.path.join(DATA_PATH,'register.csv'))
    def test_register(self):
        rp = RegisterPage(self.driver)
        file_name = r"D:\workspace\webAuto41\data\register.csv"
        print(file_name)
        data = read_csv(file_name)
        username = data[2]
        email = username + "@126.com"
        passwd = username + "123"
        confirm_passwd = passwd
        actual = rp.register(username, email, passwd, confirm_passwd, "13111223344")
        self.assertEqual(username, actual)


if __name__ == '__main__':
    unittest.main()
