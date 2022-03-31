from Base.basePage import BasePage
from selenium.webdriver.common.by import By


class IndexPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        '''
        **********************************************XPS主页面**********************************************
        '''
        self.index_logout = (By.XPATH, "//span[text()='退出']")  # 退出按钮
        self.index_role_but = (By.XPATH, "//span[@role='button']")  # 带登录用户名的按钮
        self.index_logo = (By.XPATH, "//div[@class='header']//i")  # 登录页面logo
        self.index_label_frontpage = (By.XPATH, "//span[text()=' 首页 ']")  # 首页标签
        self.index_light = (By.XPATH, "//div[@class='header-icon-wrap'][1]")  # 指示灯按钮,希望后续加id，name
        """指示灯（字段都有的情况下）"""
        """做市指示灯"""
        self.light_Mark = (By.XPATH, "//div[@class='onOrOffTitle']/span[text()='双边做市']")  # 双边做市
        self.light_Mark_open = (By.XPATH, "(//span[@class='onOrOff-text'])[1]")  # 是否开市字段
        self.light_Mark_isopen = (By.XPATH, "//div[@class='onOrOffClass']/div[2]/div[1]/div")  # 如果有做市指示灯，是否开市
        self.light_Mark_trade = (By.XPATH, "(//span[@class='onOrOff-text'])[2]")  # 交易接口字段
        self.light_Mark_istrade = (By.XPATH, "//div[@class='onOrOffClass']/div[2]/div[2]/div")  # 如果有做市指示灯，交易接口
        self.light_Mark_quotes = (By.XPATH, "(//span[@class='onOrOff-text'])[3]")  # 行情接口字段
        self.light_Mark_isquotes = (By.XPATH, "//div[@class='onOrOffClass']/div[2]/div[3]/div")  # 如果有做市指示灯，行情接口
        """X-Bond指示灯"""
        self.light_XBond = (By.XPATH, "//div[@class='onOrOffTitle']/span[text()='X-Bond']")  # X-Bond
        self.light_XBond_open = (By.XPATH, "(//span[@class='onOrOff-text'])[4]")  # 是否开市字段
        self.light_XBond_isopen = (By.XPATH, "//div[@class='onOrOffClass']/div[4]/div[1]/div")  # 如果有做市指示灯，是否开市
        self.light_XBond_trade = (By.XPATH, "(//span[@class='onOrOff-text'])[5]")  # 交易接口字段
        self.light_XBond_istrade = (By.XPATH, "//div[@class='onOrOffClass']/div[4]/div[2]/div")  # 如果有做市指示灯，交易接口
        self.light_XBond_quotes = (By.XPATH, "(//span[@class='onOrOff-text'])[6]")  # 行情接口字段
        self.light_XBond_isquotes = (By.XPATH, "//div[@class='onOrOffClass']/div[4]/div[3]/div")  # 如果有做市指示灯，行情接口
        """X-Swap指示灯"""
        self.light_XSwap = (By.XPATH, "//div[@class='onOrOffTitle']/span[text()='X-Swap']")  # X-Swap
        self.light_XSwap_open = (By.XPATH, "(//span[@class='onOrOff-text'])[7]")  # 是否开市字段
        self.light_XSwap_isopen = (By.XPATH, "//div[@class='onOrOffClass']/div[6]/div[1]/div")  # 是否开市
        self.light_XSwap_trade = (By.XPATH, "(//span[@class='onOrOff-text'])[8]")  # 交易接口字段
        self.light_XSwap_istrade = (By.XPATH, "//div[@class='onOrOffClass']/div[6]/div[2]/div")  # 交易接口
        self.light_XSwap_quotes = (By.XPATH, "(//span[@class='onOrOff-text'])[9]")  # 行情接口字段
        self.light_XSwap_isquotes = (By.XPATH, "//div[@class='onOrOffClass']/div[6]/div[3]/div")  # 行情接口
        """X-Repo指示灯"""
        self.light_XRepo = (By.XPATH, "//div[@class='onOrOffTitle']/span[text()='X-Repo']")  # X-Repo
        self.light_XRepo_open = (By.XPATH, "(//span[@class='onOrOff-text'])[10]")  # 是否开市字段
        self.light_XRepo_isopen = (By.XPATH, "//div[@class='onOrOffClass']/div[8]/div[1]/div")  # 如果有做市指示灯，是否开市
        self.light_XRepo_trade = (By.XPATH, "(//span[@class='onOrOff-text'])[11]")  # 交易接口字段
        self.light_XRepo_istrade = (By.XPATH, "//div[@class='onOrOffClass']/div[8]/div[2]/div")  # 如果有做市指示灯，交易接口
        self.light_XRepo_quotes = (By.XPATH, "(//span[@class='onOrOff-text'])[12]")  # 行情接口字段
        self.light_XRepo_isquotes = (By.XPATH, "//div[@class='onOrOffClass']/div[8]/div[3]/div")  # 如果有做市指示灯，行情接口
        """国债期货指示灯"""
        self.light_Futures = (By.XPATH, "//div[@class='onOrOffTitle']/span[text()='国债期货']")  # 国债期货
        self.light_Futures_trade = (By.XPATH, "(//span[@class='onOrOff-text'])[13]")  # 交易接口字段
        self.light_Futures_istrade = (By.XPATH, "//div[@class='onOrOffClass']/div[10]/div[1]/div")  # 如果有做市指示灯，交易接口
        self.light_Futures_quotes = (By.XPATH, "(//span[@class='onOrOff-text'])[14]")  # 行情接口字段
        self.light_Futures_isquotes = (By.XPATH, "//div[@class='onOrOffClass']/div[10]/div[2]/div")  # 如果有做市指示灯，行情接口

        """左侧导航栏"""
        self.nav_Bar_Expand = (By.XPATH, "//div[@class='menu-collapse']//i[1]")  # 导航栏拉宽
        self.sys_Management = (By.XPATH, "//span[text()='系统管理']")  # 系统管理
        # 系统管理_基础管理
        self.basic_Management = (By.XPATH, "//span[text()='基础管理']")  # 基础管理
        # 基础管理_用户管理\权限管理\系统参数
        self.user_Management = (By.XPATH, "//span[text()='用户管理']")  # 用户管理
        self.permission_Management = (By.XPATH, "//span[text()='权限管理']")  # 权限管理
        self.sys_Parameters = (By.XPATH, "//span[text()='系统参数']")  # 系统参数
        # 系统管理_关联关系维护
        self.relation_Maintenance = (By.XPATH, "//span[text()='关联关系维护']")  # 关联关系维护
        # 关联关系维护_用户和外汇席位号
        self.user_and_Forex = (By.XPATH, "//span[text()='用户和外汇席位号']")  # 用户和外汇席位号



    def get_background_color(self, locate):
        """
        获取当前元素的背景颜色
        :param locate:
        :return:
        """
        element = self.driver.find_element(*locate)
        if element.value_of_css_property("background-color") == 'rgba(68, 215, 182, 1)':
            return 'green'
        elif element.value_of_css_property("background-color") == 'rgba(255, 85, 85, 1)':
            return 'red'
        elif element.value_of_css_property("background-color") == 'rgba(255, 255, 0, 1)':
            return 'yellow'
        else:
            return 'Error'
