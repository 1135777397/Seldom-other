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
    update: 22/03/31
"""


class UserManage(unittest.TestCase):
    """回归用例——用户登录"""

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
        cls.table = cls.userManage_page.get_table_data_by_list(cls.userManage_page.userManage_table)
        logger.info("获取列表信息")

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        logger.info("关闭浏览器" + cls.userManage_page.get_current_function)
        cls.driver.quit()

    @classmethod
    def setUp(cls):
        pass

    @classmethod
    def tearDown(cls):
        pass

    @unittest.skipUnless(
        to_init().test_type == 'all' or to_init().test_type == 'usermanage',
        "非执行全部用例和login用例，跳过")
    def test_01_userManage(self):
        """获取列表信息，历史用户正常显示"""
        logger.info("test_01_userManage,查找历史用户")
        self.assertTrue(self.userManage_page.historyuser in self.table)
        logger.info(self.userManage_page.get_current_function + '获取列表信息，历史用户正常显示' + ' --> Successed')

    @unittest.skipUnless(
        to_init().test_type == 'all' or to_init().test_type == 'usermanage',
        "非执行全部用例和login用例，跳过")
    def test_02_userManage(self):
        """历史用户修改功能正常"""
        logger.info("test_02_userManage,历史用户修改功能是否正常")
        upate_xpath = pm.get_list_Xpath(dataList=self.table, data=self.userManage_page.historyuser,
                                        left=self.userManage_page.his_update_left)
        upate = (By.XPATH, upate_xpath)
        self.userManage_page.click(upate)
        self.assertFalse(self.userManage_page.is_enabled(self.userManage_page.input_username))
        self.assertFalse(self.userManage_page.is_enabled(self.userManage_page.input_name))
        logger.info("用户名、姓名不能修改判断" + ' --> Successed')
        self.userManage_page.send_keys(self.userManage_page.input_pwd, "123456")
        self.userManage_page.send_keys(self.userManage_page.input_conpwd, "123456")
        self.userManage_page.click(self.userManage_page.but_con_update)
        logger.info('修改成功')
        self.assertTrue(self.userManage_page.wait(self.userManage_page.msg_update_suc))
        logger.info(self.userManage_page.get_current_function + '历史用户修改功能正常' + ' --> Successed')

    @unittest.skipUnless(
        to_init().test_type == 'all' or to_init().test_type == 'usermanage',
        "非执行全部用例和login用例，跳过")
    def test_03_userManage(self):
        """重置密码功能正常"""
        logger.info("test_03_userManage,重置密码功能是否正常")
        reset_pw_Xpath = pm.get_list_Xpath(dataList=self.table, data=self.userManage_page.historyuser,
                                           left=self.userManage_page.his_reset_pwd)
        reset_pw = (By.XPATH, reset_pw_Xpath)
        self.userManage_page.click(reset_pw)
        self.userManage_page.click(self.userManage_page.his_rp_con)
        self.userManage_page.wait(self.userManage_page.msg_rp_suc)
        logger.info("重置密码成功！")
        self.userManage_page.sleep(1)
        self.index_page.click(self.index_page.index_logout)
        self.login_page.send_keys(self.login_page.account, self.userManage_page.historyuser)
        self.login_page.send_keys(self.login_page.password, '123456')
        self.login_page.click(self.login_page.login_but)
        self.index_page.wait(self.index_page.index_logout)
        logger.info("重置密码校验成功！")
        logger.info(self.userManage_page.get_current_function + '重置密码功能正常' + ' --> Successed')

    @unittest.skipUnless(
        to_init().test_type == 'all' or to_init().test_type == 'usermanage' ,
        "非执行全部用例和login用例，跳过")
    def test_04_userManage(self):
        """新增用户"""
        logger.info("test_04_userManage,历史用户第三方用户绑定功能是否正常")
        user_bind_Xpath = pm.get_list_Xpath(dataList=self.table, data=self.userManage_page.historyuser,
                                            left=self.userManage_page.his_user_bind)
        user_bind = (By.XPATH, user_bind_Xpath)
        self.userManage_page.click(user_bind)
        self.userManage_page.send_keys(self.userManage_page.user_id, "WZH")
        self.userManage_page.select_dropDownBox_by_value(element=self.userManage_page.system_code, value="xir")
        self.userManage_page.sleep(2)
        self.userManage_page.click(self.userManage_page.but_con_user_bind)
        self.userManage_page.sleep(2)
