"""
Exceptions that may happen in all the seldom code.
在所有很少见的代码中可能发生的异常。
"""


class SeldomException(Exception):
    """
    Base poium exception.
    基础 poium 异常
    """

    def __init__(self, msg=None, screen=None, stacktrace=None):
        self.msg = msg
        # 屏幕
        self.screen = screen
        # 堆栈跟踪
        self.stacktrace = stacktrace

    def __str__(self):
        exception_msg = "Message: %s\n" % self.msg
        if self.screen is not None:
            exception_msg += "Screenshot: available via screen\n"
        if self.stacktrace is not None:
            stacktrace = "\n".join(self.stacktrace)
            exception_msg += "Stacktrace:\n%s" % stacktrace
        return exception_msg


class NotFindElementError(SeldomException):
    """
    No element errors were found
    未发现元素错误
    """
    pass


class TestFixtureRunError(SeldomException):
    """
    Test fixture run error
    测试夹具运行错误
    """
    pass


class FileTypeError(SeldomException):
    """
    Data file type error
    数据文件类型错误
    """
    pass
