import os
import time
import inspect
from loguru import logger
from seldom.Bean_seldom.BrowserConfig import BrowserConfig
from seldom.Bean_seldom.SeldomConfig import SeldomConfig

"""stack_t获取类或函数的参数的信息，一个列表"""
stack_t = inspect.stack()
ins = inspect.getframeinfo(stack_t[1][0])
file_dir = os.path.dirname(os.path.abspath(ins.filename))
report_dir = os.path.join(file_dir, "reports")
if os.path.exists(report_dir) is False:
    os.mkdir(report_dir)


now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
if BrowserConfig.LOG_PATH is None:
    BrowserConfig.LOG_PATH = os.path.join(os.getcwd(), "reports", now_time + "_log.log")
if BrowserConfig.REPORT_PATH is None:
    BrowserConfig.REPORT_PATH = os.path.join(os.getcwd(), "reports", now_time + "_result.html")

print(BrowserConfig.LOG_PATH)
logger.add(BrowserConfig.LOG_PATH, encoding="utf-8")

colorLog = True


def debug(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    if SeldomConfig.debug is False:
        print(now + " [DEBUG] " + str(msg))
    if colorLog is True:
        return logger.debug(msg)
    else:
        msg = msg.encode('gbk', 'ignore').decode('gbk', "ignore")
        return logger.debug(msg)


def info(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    if SeldomConfig.debug is False:
        print(now + " [INFO] " + str(msg))
    if colorLog is True:
        return logger.info(msg)
    else:
        msg = msg.encode('gbk', 'ignore').decode('gbk', "ignore")
        return logger.info(msg)


def error(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    if SeldomConfig.debug is False:
        print(now + " [ERROR] " + str(msg))
    if colorLog is True:
        return logger.error(msg)
    else:
        msg = msg.encode('gbk', 'ignore').decode('gbk', "ignore")
        return logger.info(msg)


def warn(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    if SeldomConfig.debug is False:
        print(now + " [WARNING] " + str(msg))
    if colorLog is True:
        return logger.warning(msg)
    else:
        msg = msg.encode('gbk', 'ignore').decode('gbk', "ignore")
        return logger.warning(msg)


def printf(msg):
    if colorLog is True:
        return logger.success(msg)
    else:
        msg = msg.encode('gbk', 'ignore').decode('gbk', "ignore")
        return logger.success(msg)

