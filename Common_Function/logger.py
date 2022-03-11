import logging
import logging.handlers
import os
import time
from Common_Function.dateTimeTool import DateTimeTool
from Common_Function.readConfig import ReadConfig


def getlevel(level):
    if level == 'debug':
        return logging.DEBUG
    elif level == 'info':
        return logging.INFO
    elif level == 'warning':
        return logging.WARNING
    elif level == 'error':
        return logging.ERROR
    elif level == 'critical':
        return logging.CRITICAL
    elif level == 'notset':
        return logging.NOTSET
    else:
        print("没有对应的字段，或字段名有误未小写，默认为ERROR级别")
        return logging.ERROR


class Logger(object):
    """
    author: kawi
    time: 22/03/02
    update: kawi-22/03/08
    """

    # logger:名称
    # level:处理器日志级别
    def __init__(self, logger):
        """
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        """
        # 路径为当前文件上一级再上一级
        self.path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'logs')
        # print(os.path.dirname(os.path.dirname(__file__)))
        # print(self.path)
        """
            当前自己写时间后续完善
        """
        time_with_Y_m_d = DateTimeTool.getNowTime('%Y-%m-%d')
        # print(time_with_Y_m_d)
        time_with_Y_m_d_H = DateTimeTool.getNowTime("%Y-%m-%d_%H")
        # print(time_with_Y_m_d_H)
        dir_path = os.path.join(self.path, time_with_Y_m_d)
        # dir_file_path = os.path.join(dir_path, time_with_Y_m_d)
        # print(dir_path, time_with_Y_m_d_H_M_S)
        # 判断文件夹是否存在，不存在则创建
        if os.path.isdir(dir_path):
            pass
        else:
            os.makedirs(dir_path)
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # self.log_name = '{0}.log'.format(dir_path)
        # 由于需要多次创建logger对象，所以有较低概率会产生1个以上的日志文件，此处进行一次修正
        try:
            last_log_name = os.listdir(dir_path)[-1]
            # 从文件名中获取时间戳
            last_log_timestamp = time.mktime(
                time.strptime(last_log_name[:last_log_name.find('.')], "%Y-%m-%d"))
            now_log_timestamp = time.mktime(time.strptime(time_with_Y_m_d, "%Y-%m-%d"))
            if now_log_timestamp - last_log_timestamp < 3600:
                # 创建一个handler，用于写入日志文件
                log_name = dir_path + '/' + last_log_name
                # print("last" + log_name)
            else:
                log_name = dir_path + '/' + time_with_Y_m_d + '.log'
                # print("new" + log_name)
        except IndexError:
            log_name = dir_path + '/' + time_with_Y_m_d + '.log'
            # print("except"+log_name)

        # 获取配置文件中的日志等级
        level = ReadConfig().get_logger_level()
        self.lever_file = level['log_level_file']
        # print(self.lever_file)
        self.level_console = level['log_level_console']
        # 输出日志的handler处理器
        file_handler = logging.handlers.TimedRotatingFileHandler(filename=log_name, when='H', interval=1,
                                                                 encoding='utf-8')
        file_handler.setLevel(getlevel(self.lever_file))
        file_handler.setFormatter(formatter)
        # 输出到控制台的handler处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(getlevel(self.level_console))
        console_handler.setFormatter(formatter)
        #
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def getlogger(self):
        return self.logger
