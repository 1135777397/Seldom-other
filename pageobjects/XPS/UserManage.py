from Base.basePage import BasePage
from selenium.webdriver.common.by import By


class UserManagePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        '''
        **********************************************XPS用户管理页面**********************************************
        '''
        self