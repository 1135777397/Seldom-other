from Base.basePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        '''
        **********************************************XPS内部登录**********************************************
        '''

        self.account = (By.XPATH, "//input[@placeholder='请输入帐号']")  # 用户名框
        self.password = (By.XPATH, '//input[@placeholder="请输入密码"]')  # 密码
        self.login_but = (By.XPATH, "//button[@type='button']")  # 登录按钮
        self.acc_null_raise = (By.XPATH, "//p[text()='帐号不能为空！']")  # 账号不能为空提示
        self.pass_null_raise = (By.XPATH, "//p[text()='密码不能为空！']")  # 密码不能为空提示
        self.acc_notexist_raise = (By.XPATH, "//p[text()='用户已禁用或用户不存在！']")  # 用户已禁用或用户不存在
        self.pass_error_raise = (By.XPATH, "//p[text()='用户密码错误！1次,错误6次后该用户将被禁用!']")  # 用户密码错误

        # 登录成功之后的页面按钮
        self.i_logout = (By.XPATH, "//*[contains(.,'" + "退出" + "')]")  # 退出按钮
