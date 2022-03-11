import os
from configparser import ConfigParser
import logging
# from Common_Function.logger import Logger

# 系统配置文件路径
configPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config/config.ini')

# logger = Logger(logger="ReadConfig").getlogger()
# 因为logger里面导入了readconfig方法，所以无法再引用logger方法

class ReadConfig:
    """
    author: kawi
    time: 22/03/08
    update: 22/03/11
    """

    def __init__(self):
        self.config = ConfigParser()
        self.config.read(configPath, encoding="UTF-8")

    def get_browser_type(self):
        browserName = self.config.get("BROWSERTYPE", "browserName")
        # self.logger.debug("Get the browserName in the config file")
        return browserName

    # 隐式等待时间
    def get_browser_attribute(self):
        implicitly_wait = self.config.get("BROWSERATTRIBUTE", "implicitly_wait")
        # self.logger.debug("Get the implicitly_wait in the config file")
        return implicitly_wait

    def get_test_server(self):
        url = self.config.get("TESTSERVER", "url")
        # self.logger.debug("Get the url in the config file")
        return url

    def get_test_account(self):
        account = self.config.get("TESTACCOUNT", "account")
        password = self.config.get("TESTACCOUNT", "password")
        name = self.config.get("TESTACCOUNT", "name")
        account_value = {'account': account, 'password': password, 'name': name}
        # logger.debug("Get the test_account in the config file")
        return account_value

    def get_database(self):
        DBtype = self.config.get("DATABASE", "type")
        DBuser = self.config.get("DATABASE", "user")
        DBpassword = self.config.get("DATABASE", "password")
        DBdatabase = self.config.get("DATABASE", "database")
        DBhost = self.config.get("DATABASE", "host")
        DBport = self.config.get("DATABASE", "port")
        value = {'type': DBtype, 'user': DBuser, 'password': DBpassword, 'database': DBdatabase, 'host': DBhost,
                 'port': DBport}
        # logger.debug("Get the database in the config file")
        return value

    def get_logger_level(self):
        log_level_file = self.config.get("LOGGER", "log_level_file")
        log_level_console = self.config.get("LOGGER", "log_level_console")
        value = {'log_level_file': log_level_file, 'log_level_console': log_level_console}
        # logger.debug("Get the logger_level in the config file——file_level:{0}——console_level:{1}".format(log_level_file,
        #                                                                                                  log_level_console))
        return value

    def get_test_data(self, *args):
        """
        从配置文件中获取测试数据，接收可变数量的参数
        :param args:
        :return: 返回字典
        """
        a = {}
        for i in args:
            a[i] = self.config.get("TESTDATA", i)
        # logger.debug("Get the test_data in the config file")
        return a
