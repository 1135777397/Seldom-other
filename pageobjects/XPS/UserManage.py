from Base.basePage import BasePage
from selenium.webdriver.common.by import By


class UserManagePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.historyuser = 'AThistory'
        '''
        **********************************************XPS用户管理页面**********************************************
        '''
        self.userManage_table = (By.XPATH, "//table[@class='el-table__body']")  # 表格
        self.his_update_left = "(//span[text()=' 修改 '])"
        self.input_name = (By.XPATH, "//input[@placeholder='请输入用户名']")
        self.