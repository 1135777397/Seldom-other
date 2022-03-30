# -*- coding:utf-8 -*-
from Common_Function.logger import Logger

logger = Logger(logger="positionMethod").getlogger()

class positionMethod:
    """
        author: kawi
        time: 22/03/30
        update:
    """

    @classmethod
    def get_list_Xpath(cls, dataList: list, data, left, right=''):
        """
        获取Xpath
        :param left:左侧的xpath
        :param right: 右侧的xpath
        :return:
        """
        if data in dataList:
            i = dataList.index(data)
            logger.info("获取Xpath为:"+left+ "[{}]".format(i+1) + right)
            return ''.join(left + "[{}]".format(i+1) + right)
        else:
            logger.error('{0}不在列表{}中'.format(data,dataList))
            return None
