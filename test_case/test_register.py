import unittest

from lib.data_lib import read_csv
from page.register_page import RegisterPage


class RegisterTestCase(unittest.TestCase):
    def test_register(self):
        rp = RegisterPage()
        file_name = r"D:\workspace\webAuto41\data\register.csv"
        data = read_csv(file_name)
        username = data[2]
        email = username+"@126.com"
        passwd = username+"123"
        confirm_passwd = passwd
        actual = rp.register(username,email,passwd,confirm_passwd,"13111223344")
        self.assertEqual(username, actual)


if __name__ == '__main__':
    unittest.main()
