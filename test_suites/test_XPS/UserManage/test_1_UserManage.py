import time
import unittest

from Common_Function.logger import Logger
from test_suites.test_XPS import *
from Common_Function.dateTimeTool import DateTimeTool
from Base.positionMethod import positionMethod as pm
from selenium.webdriver.common.by import By

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
        cls.userManage_page = get_userManage_page(cls.driver)
        cls.user_info = ini.user_info
        cls.user_admin = ini.user_admin
        cls.nowTime = DateTimeTool().getNowTime(format="%H:%M:%S")
        logger.info('当前时间为：' + cls.nowTime)
        logger.info("开启浏览器" + cls.login_page.get_current_function)
        cls.login_page.send_keys(cls.login_page.account, cls.user_info["userName"])
        cls.login_page.send_keys(cls.login_page.password, cls.user_info["password"])
        cls.login_page.click(cls.login_page.login_but)
        cls.index_page.click(cls.index_page.nav_Bar_Expand)
        cls.index_page.click(cls.index_page.sys_Management)
        cls.index_page.click(cls.index_page.basic_Management)
        cls.index_page.click(cls.index_page.user_Management)

    @classmethod
    def tearDown(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        logger.info("关闭浏览器" + cls.login_page.get_current_function)
        cls.driver.quit()

    @unittest.skipUnless(
        to_init().test_type == 'all' or to_init().test_type == 'usermanage',
        "非执行全部用例和login用例，跳过")
    def test_01_userManage(self):
        """获取列表信息，历史用户正常显示"""
        logger.info("test_01_userManage,查找历史用户")
        table = self.userManage_page.get_table_data_by_list(self.userManage_page.userManage_table)
        self.assertTrue(self.userManage_page.historyuser in table)
        logger.info(self.userManage_page.get_current_function + '获取列表信息，历史用户正常显示' + ' --> Successed')

    @unittest.skipUnless(
        to_init().test_type == 'all' or to_init().test_type == 'usermanage' or to_init().test_type == 'test',
        "非执行全部用例和login用例，跳过")
    def test_02_userManage(self):
        """历史用户修改功能正常"""
        logger.info("test_02_userManage,历史用户修改功能是否正常")
        table = self.userManage_page.get_table_data_by_list(self.userManage_page.userManage_table)
        logger.info(table)
        upate_xpath = pm.get_list_Xpath(dataList=table, data=self.userManage_page.historyuser,
                                        left=self.userManage_page.his_update_left)
        logger.info(type(upate_xpath))
        upate = (By.XPATH, upate_xpath)
        self.userManage_page.click(upate)

        time.sleep(3)
