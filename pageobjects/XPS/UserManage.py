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
        self.input_username = (By.XPATH, "//input[@placeholder='请输入用户名']")
        self.input_name = (By.XPATH, "//input[@placeholder='请输入姓名']")
        self.input_pwd = (By.XPATH, "//input[@placeholder='请输入密码']")
        self.input_conpwd = (By.XPATH, "//input[@placeholder='请确认密码']")
        self.but_con = (By.XPATH, "//div[@aria-label='修改用户']//span[text()='确 定']")
        self.msg_update_suc = (By.XPATH, "//p[text()='修改成功']")
        self.his_reset_pwd = "(//span[text()=' 重置密码 '])"
        self.his_rp_con = (By.XPATH, "(//div[@class='el-message-box__btns']//button)[2]")
        self.msg_rp_suc = (By.XPATH, "//p[text()='密码重置成功']")
