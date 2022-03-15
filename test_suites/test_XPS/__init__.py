from Common_Function.browserEngine import BrowserEngine
from Common_Function.HTMLTestReportCN import DirAndFiles
from Common_Function.connectDataBase import ConnectDataBase
from pageobjects.XPS.Login import LoginPage
from pageobjects.XPS.Index import IndexPage
from pageobjects.XPS.UserManage import UserManagePage

"""
    author: kawi
    time: 22/03/10
    update: 22/03/11 kawi
"""


class to_init():
    def __init__(self):
        self.user_info = {"userName": "AutoTest", "password": "123456"}
        self.user_admin = {"userName": "admin", "password": "123456"}

    def get_driver(self):
        """打开网页并获取driver"""
        browser = BrowserEngine(self)
        driver = browser.open_browser(self)
        return driver

    def clean_test_data(self):
        """清理测试数据"""
        pass


def get_daf():
    """
    获取测试报告对象
    :return:
    """
    return DirAndFiles()


def get_login_page(driver):
    """
    获取XPS登录页面控件
    :return:
    """
    return LoginPage(driver)


def get_index_page(driver):
    """
    获取XPS主页面
    :return:
    """
    return IndexPage(driver)


def get_userManage_page(driver):
    """
    获取XPS主页面
    :return:
    """
    return UserManagePage(driver)
