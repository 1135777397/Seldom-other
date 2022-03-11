import unittest

from Common_Function.logger import Logger
from test_suites.test_XPS.Login import *

logger = Logger(logger="XPS_Login").getlogger()
"""
    author: kawi
    time: 22/03/10
    update:
"""


class Login(unittest.TestCase):
    """登录测试"""

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        ini = to_init()
        cls.driver = ini.get_driver()
        cls.daf = get_daf()
        cls.login_page = get_login_page(cls.driver)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def setUp(self):
        pass

    def test_01_login(self):
        """登录"""
        self.login_page.send_keys(self.login_page.account, "admin")
        self.login_page.send_keys(self.login_page.password, "123456")
        self.login_page.click(self.login_page.login_but)
        self.assertTrue(self.login_page.wait((self.login_page.login_but)))
        print(self.login_page.get_current_function())
        logger.info(self.login_page.get_current_function() + ' --> Successed')
