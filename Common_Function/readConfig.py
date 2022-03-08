import os
from configparser import ConfigParser

# 系统配置文件路径
configPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config/config.ini')


class ReadConfig:
    """
    author: kawi
    time: 22/03/08
    update:
    """

    def __init__(self):
        self.config = ConfigParser()
        self.config.read(configPath, encoding="UTF-8")

    def get_browser_type(self):
        browserName = self.config.get("BROWSERTYPE", "browserName")
        return browserName

    # 隐式等待时间
    def get_browser_attribute(self):
        implicitly_wait = self.config.get("BROWSERATTRIBUTE", "implicitly_wait")
        return implicitly_wait

    def get_test_server(self):
        url = self.config.get("TESTSERVER", "url")
        return url

    def get_test_account(self):
        account = self.config.get("TESTACCOUNT", "account")
        password = self.config.get("TESTACCOUNT", "password")
        name = self.config.get("TESTACCOUNT", "name")
        account_value = {'account': account, 'password': password, 'name': name}
        return account_value

    def get_database(self):
        DBtype = self.cf.get("DATABASE", "type")
        DBuser = self.cf.get("DATABASE", "user")
        DBpassword = self.cf.get("DATABASE", "password")
        DBdatabase = self.cf.get("DATABASE", "database")
        DBhost = self.cf.get("DATABASE", "host")
        DBport = self.cf.get("DATABASE", "port")
        value = {'type': DBtype, 'user': DBuser, 'password': DBpassword, 'database': DBdatabase, 'host': DBhost,
                 'port': DBport}
        return value

    def get_logger_level(self):
        log_level_file = self.config.get("LOGGER", "log_level_file")
        log_level_console = self.config.get("LOGGER", "log_level_console")
        value = {'log_level_file': log_level_file, 'log_level_console': log_level_console}
        return value

    def get_test_data(self, *args):
        """
        从配置文件中获取测试数据，接收可变数量的参数
        :param args:
        :return: 返回字典
        """
        a = {}
        for i in args:
            a[i] = self.cf.get("TESTDATA", i)
        return a
