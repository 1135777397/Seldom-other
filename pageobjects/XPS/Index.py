from Base.basePage import BasePage
from selenium.webdriver.common.by import By


class IndexPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        '''
        **********************************************XPS主页面**********************************************
        '''
