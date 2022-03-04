# -*- coding:utf-8 -*-

import datetime
import time
import calendar


class DateTimeTool:
    """
        author: kawi
        time: 22/03/03
        update:
    """
    # 修饰符对应的函数不需要实例化，不需要 self 参数
    @classmethod
    def getNowTime(cls, format='%Y-%m-%d %H:%M:%S'):
        # strftime(format) 获取格式化的时间
        # datetime.now()放回当前时间的毫秒精度
        return datetime.datetime.now().strftime(format)

    @classmethod
    def getNowDate(cls, format='%Y-%m-%d'):
        # 获取当前日期
        return datetime.date.today().strftime(format)

    @classmethod
    def getNowTimeStampWithSecond(cls):
        # 返回时间戳
        return int(time.time())

    @classmethod
    def getNowTimeStampWithMillisecond(cls):
        # round+0.5 向下取整数
        return int(round(time.time() * 1000))

    @classmethod
    def timeStampToDateTime(cls, timeStamp: int, is_with_millisecond=False):
        """
        :param timeStamp:时间戳数据
        :param is_with_millisecond:是否包含毫秒，默认false，可以使用getNowTimeStampWithSecond
        :return: 当前时间
        """
        if is_with_millisecond:
            timeStamp = timeStamp / 1000
        resultDateTime = datetime.datetime.fromtimestamp(timeStamp)
        return resultDateTime

    @classmethod
    def getWeekDay(cls):
        """
        获得今天星期几，从1开始
        :return:
        """
        return datetime.datetime.now().weekday() + 1

    @classmethod
    def getHowDaysAgo(cls, nowDateTime, nowDateTime_format='%Y-%m-%d %H:%M:%S', howDaysAgo=0):
        """
        显示几天前日期
        :param nowDateTime:当前日期,以%Y-%m-%d %H:%M:%S格式
        :param nowDateTime_format:默认%Y-%m-%d %H:%M:%S
        :param howDaysAgo:减去的日期
        :return:
        """
        nowDateTime = datetime.datetime.strptime(str(nowDateTime), nowDateTime_format)
        resultDateTime = nowDateTime - datetime.timedelta(days=howDaysAgo)
        return resultDateTime

    @classmethod
    def dateTimeToStr(cls, theDateTime, format='%Y-%m-%d'):
        """
        日期格式化
        :param theDateTime:
        :param format:
        :return:
        """
        return theDateTime.strftime(format)

    @classmethod
    def strToDateTime(cls, str, str_format):
        """
        日期解析
        :param str:
        :param str_format:
        :return:
        """
        dst_dateTime = datetime.datetime.strptime(str, str_format)
        return dst_dateTime

    @classmethod
    def getHowYearsAgo(cls, nowDate, howYearsAgo=0, nowDate_format='%Y-%m-%d'):
        resultDate = cls.getHowDaysAgo(nowDate, nowDate_format, howYearsAgo * 366)
        return resultDate

    @classmethod
    def getCurrentMonthFirstDayOrLastDay(cls, type=1):
        """获取当前月第一天或者最后一天日期
        Args:
            type (int, optional): 第一天:1，最后一天:-1

        Returns:
            [type]: [description]
        """
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        last_day = calendar.monthrange(year, month)[1]
        if type == 1:
            start = datetime.date(year, month, 1)
            return start
        if type == -1:
            end = datetime.date(year, month, last_day)
            return end
