"""
Seldom bean file
"""
"""
    author: kawi
    time: 22/04/07
    update: 
"""


class SeldomConfig:
    """
    Seldom browser driver
    :param driver: driver
    :param timeout:设置超时时间，默认10秒。
    :param debug: debug模式，设置为True不生成测试HTML测试报告，默认为False
    :param base_url:针对HTTP接口测试的参数，设置全局的URL。
    """
    driver = None
    timeout = 10
    debug = False
    base_url = None
