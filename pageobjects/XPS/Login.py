from Base.basePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        '''
        **********************************************CDS内部登录**************************************
        '''

        self.account = (By.XPATH, "//input[@placeholder='请输入帐号']")  # 用户名框
        self.password = (By.XPATH, '//input[@placeholder="请输入密码"]')  # 密码
        self.login_but = (By.XPATH, "//button[@type='button']")  # 登录按钮

        # 登录成功之后的页面按钮
        self.i_logout = (By.XPATH, "//*[contains(.,'" + "退出" + "')]")  # 退出按钮
