import time

from selenium.webdriver.common.by import By

from page.LoginPage import LoginPage


class UpdateUserPage(LoginPage):
    def __init__(self, driver):
        # super().__init__() # 这里继承了父类的driver
        self.driver = driver  # driver 从外面传递进来，不要重新实例化
        print("初始化")

    # 点击左上角的用户中心
    def ele_user(self):
        self.driver.find_element(By.XPATH, '//font[@id="ECS_MEMBERZONE"]/font/a[1]').click()

    # 点击左侧列表的用户中心
    def ele_user_center(self):
        self.driver.find_element(By.XPATH, '/html/body/div[8]/div[1]/div/div/div/div/a[2]').click()

    # 输入修改后的邮箱
    def ele_email(self):
        self.driver.find_element(By.NAME, 'email').send_keys('342352435@qq.com')

    # 输入修改后的手机号
    def ele_mobile(self):
        self.driver.find_element(By.NAME, 'extend_field5').send_keys('13959795452')

    # 点击确认修改按钮
    def ele_submit(self):
        self.driver.find_element(By.NAME, 'submit').click()

    def update_user(self):  # 这里不要调用其他page页面
        time.sleep(5)
        self.ele_user()
        time.sleep(5)
        self.ele_user_center()
        self.ele_email()
        self.ele_mobile()
        self.ele_submit()
        self.driver.quit()

# 登录后的窗口，使用的的driver 与后面的driver2 不同，所以会打开两个driver，出现以上问题
# 解决办法就是要统一两个diver，使用同一个driver
