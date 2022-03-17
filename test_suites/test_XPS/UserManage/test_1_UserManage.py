import unittest

from Common_Function.logger import Logger
from test_suites.test_XPS import *
from Common_Function.dateTimeTool import DateTimeTool

logger = Logger(logger="XPS_UserManage").getlogger()
"""
    author: kawi
    time: 22/03/16
    update: 
"""

class UserManage(unittest.TestCase):
    """回归用例——用户登录"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @classmethod
    def setUp(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        ini = to_init()
        cls.driver = ini.get_driver()
        cls.daf = get_daf()
        cls.login_page = get_login_page(cls.driver)
        cls.index_page = get_index_page(cls.driver)
        cls.user_info = ini.user_info
        cls.user_admin = ini.user_admin
        cls.nowTime = DateTimeTool().getNowTime(format="%H:%M:%S")
        logger.info('当前时间为：' + cls.nowTime)
        logger.info("开启浏览器" + cls.login_page.get_current_function)

    @classmethod
    def tearDown(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        logger.info("关闭浏览器" + cls.login_page.get_current_function)
        cls.driver.quit()
