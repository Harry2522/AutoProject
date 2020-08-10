import time

from selenium.webdriver.common.by import By

from lib.path_lib import BASE_URL


class LoginPage():
    # init中是初始化属性，类中如果要被覆值被其他地方使用，要加self
    def __init__(self, driver):
        print("初始化")
        # 元素定位符
        self.driver = driver  # 每个page页面初始化的时候，都是这样，从外面接收一个driver
        self.url = BASE_URL + "user.php"

        self.locator_username = (By.NAME, "username")
        self.locator_password = (By.NAME, "password")
        self.locator_submit = (By.NAME, "submit")
        self.locator_assert = (By.XPATH, '//font[@id="ECS_MEMBERZONE"]/font/font')

    def ele_username(self, username):
        self.driver.find_element(*self.locator_username).send_keys(username)

    def ele_password(self, password):
        self.driver.find_element(*self.locator_password).send_keys(password)

    def ele_submit(self):
        self.driver.find_element(*self.locator_submit).click()

    def assert_result(self):
        actual_result = self.driver.find_element(*self.locator_assert).text
        return actual_result

    def login(self, username, password):
        self.driver.get(url=self.url)
        self.ele_username(username)
        self.ele_password(password)
        self.ele_submit()
        time.sleep(2)
        actual_result = self.assert_result()

        # 关闭浏览器
        # self.driver.quit()  #这里也要关闭，不然登录后窗口就关闭了，
        #                       后续的操作时要在原来的窗口进行的
        return actual_result

# lp = LoginPage()
# lp.login()
