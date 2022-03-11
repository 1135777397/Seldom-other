from Common_Function.browserEngine import BrowserEngine
from framework.HTMLTestReportCN import DirAndFiles
from framework.ConnectDataBase import ConnectDataBase
from pageobjects.XPS.Login import LoginPage

"""
    author: kawi
    time: 22/03/10
    update:
"""


class to_init():
    # def __init__(self):
    # self.user_info = {"userName":"hahaha", "password":"ahahah"}

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

# def quit_driver(driver) -> None:
#     """
#     关闭driver
#     :param driver:
#     """
#     driver.quit()
