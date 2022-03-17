import unittest

from Common_Function.logger import Logger
from test_suites.test_XPS import *

logger = Logger(logger="XPS_Login1").getlogger()
"""
    author: kawi
    time: 22/03/10
    update: 22/03/11 kawi
"""


class Login1(unittest.TestCase):
    """测试点登录功能"""

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        ini = to_init()
        cls.test_type = ini.test_type
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

    @unittest.skipUnless(
        to_init().test_type == 'all' or to_init().test_type == 'login' or to_init().test_type == 'test',
        "非执行全部用例和login用例，跳过")
    def test_01_login(self):
        """什么也不输入登录"""
        self.login_page.click(self.login_page.login_but)
        self.assertTrue(self.login_page.wait(self.login_page.acc_null_raise))
        logger.info(self.login_page.get_current_function + '不输入账号、密码' + ' --> Successed')

    @unittest.skipUnless(
        to_init().test_type == 'all' or to_init().test_type == 'login' or to_init().test_type == 'test',
        "非执行全部用例和login用例，跳过")
    def test_02_login(self):
        """只输入账号"""
        self.login_page.send_keys(self.login_page.account, "admin")
        self.login_page.click(self.login_page.login_but)
        self.assertTrue(self.login_page.wait(self.login_page.pass_null_raise))
        logger.info(self.login_page.get_current_function + '只输入账号' + ' --> Successed')

    @unittest.skipUnless(
        to_init().test_type == 'all' or to_init().test_type == 'login' or to_init().test_type == 'test',
        "非执行全部用例和login用例，跳过")
    def test_03_login(self):
        """只输入密码"""
        self.login_page.delete(self.login_page.account)
        self.login_page.send_keys(self.login_page.password, '123456')
        self.login_page.click(self.login_page.login_but)
        self.assertTrue(self.login_page.wait(self.login_page.acc_null_raise))
        logger.info(self.login_page.get_current_function + '只输入密码' + ' --> Successed')

    @unittest.skipUnless(
        to_init().test_type == 'all' or to_init().test_type == 'login' or to_init().test_type == 'test',
        "非执行全部用例和login用例，跳过")
    def test_04_login(self):
        """账号不存在"""
        self.login_page.clear(self.login_page.password)
        self.login_page.send_keys(self.login_page.account, "iklm")
        self.login_page.send_keys(self.login_page.password, "123456")
        self.login_page.click(self.login_page.login_but)
        self.assertTrue(self.login_page.wait(self.login_page.acc_notexist_raise))
        logger.info(self.login_page.get_current_function + "账号不存在" + '--> Successed')

    @unittest.skipUnless(
        to_init().test_type == 'all' or to_init().test_type == 'login' or to_init().test_type == 'test',
        "非执行全部用例和login用例，跳过")
    def test_05_login(self):
        """密码不正确"""
        self.login_page.clear(self.login_page.account)
        self.login_page.clear(self.login_page.password)
        self.login_page.send_keys(self.login_page.account, "admin")
        self.login_page.send_keys(self.login_page.password, "ujin")
        self.login_page.click(self.login_page.login_but)
        self.assertTrue(self.login_page.wait(self.login_page.pass_error_raise))
        logger.info(self.login_page.get_current_function + "密码不正确" + '--> Successed')

    @unittest.skipUnless(
        to_init().test_type == 'all' or to_init().test_type == 'login' or to_init().test_type == 'test',
        "非执行全部用例和login用例，跳过")
    def test_06_login(self):
        """登录成功"""
        self.login_page.clear(self.login_page.account)
        self.login_page.clear(self.login_page.password)
        self.login_page.send_keys(self.login_page.account, "admin")
        self.login_page.send_keys(self.login_page.password, "123456")
        self.login_page.click(self.login_page.login_but)
        self.assertTrue(self.login_page.wait(self.login_page.i_logout))
        # print(self.login_page.get_current_function())
        logger.info(self.login_page.get_current_function + '登录成功' + ' --> Successed')
