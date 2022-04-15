import os
import re
import ast
import inspect
import json as sys_json
import unittest
import webbrowser
from seldom.Base_seldom.driver.driver import Browser
from seldom.Bean_seldom.BrowserConfig import BrowserConfig
from seldom.Bean_seldom.SeldomConfig import SeldomConfig
from seldom.Base_seldom.testCase.loader_extend import seldomTestLoader
from seldom.Base_seldom.method.exceptions import SeldomException
from XTestRunner import HTMLTestRunner
from XTestRunner import XMLTestRunner
from selenium.webdriver.remote.webdriver import WebDriver as SeleniumWebDriver
from seldom.Base_seldom.logging import log
from seldom.Base_seldom.testCase.DebugTestRunner import DebugTestRunner

INIT_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "__init__.py")
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open(INIT_FILE, 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

seldom_str = """
              __    __              
   ________  / /___/ /___  ____ ____ 
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v{v}
-----------------------------------------
                             @itest.info
""".format(v=version)


class TestMain(object):
    """
    Reimplemented Seldom Runner, Support for Web and API
    重新实现 Seldom Runner，支持 Web 和 API
    """
    # 测试套件
    TestSuits = []

    def __init__(self, path=None, browser=None, base_url=None, debug=False, timeout=10,
                 report=None, title="Seldom Test Report", tester="Tester", description="Test case execution",
                 rerun=0, save_last_run=False, language="zh-CN", whitelist=[], blacklist=[], auto=True):
        """
        runner test case
        :param path:指定测试目录或文件。
        :param browser:针对Web UI测试需要指定浏览器（"chrome"、"firefox" 等）。
        :param base_url:针对HTTP接口测试的参数，设置全局的URL。
        :param report:自定义测试报告的名称，默认格式为2020_04_04_11_55_20_result.html。
        :param title:指定测试报告标题。
        :param tester:指定测试人员, 默认Anonymous。
        :param description:指定测试报告描述。
        :param debug: debug模式，设置为True不生成测试HTML测试报告，默认为False
        :param timeout:设置超时时间，默认10秒。
        :param rerun:设置失败重新运行次数，默认为 0。
        :param save_last_run:设置只保存最后一次的结果，默认为False。
        :param language:设置HTML报告中英文，默认en, 中文zh-CN。
        :param whitelist:用例标签（label）设置白名单。
        :param blacklist:用例标签（label）设置黑名单。
        :param auto:是否自动
        :return:
        """
        print(seldom_str)
        self.path = path
        self.browser = browser
        print(browser,"++++++",self.browser)
        self.report = report
        self.title = BrowserConfig.REPORT_TITLE = title
        self.tester = tester
        self.description = description
        self.debug = debug
        self.rerun = rerun
        self.save_last_run = save_last_run
        self.language = language
        self.whitelist = whitelist
        self.blacklist = blacklist

        # 判断字段是否是该类型的数据
        if isinstance(timeout, int) is False:
            raise TypeError("Timeout {} is not integer.".format(timeout))

        if isinstance(debug, bool) is False:
            raise TypeError("Debug {} is not Boolean type.".format(debug))

        SeldomConfig.timeout = timeout
        SeldomConfig.debug = debug
        SeldomConfig.base_url = base_url

        # ----- Global open browser -----
        self.open_browser()

        """
        如果没有指定测试目录，就在当前文件中查询测试用例
        seldomTestLoader.discover(file_dir, this_file)
        file_dir目录下的this_file命名的文件
        """
        if self.path is None:
            stack_t = inspect.stack()
            ins = inspect.getframeinfo(stack_t[1][0])
            print(ins.filename)
            file_dir = os.path.dirname(os.path.abspath(ins.filename))
            file_path = ins.filename
            if "\\" in file_path:
                this_file = file_path.split("\\")[-1]
            elif "/" in file_path:
                this_file = file_path.split("/")[-1]
            else:
                this_file = file_path
            self.TestSuits = seldomTestLoader.discover(file_dir, this_file)
        else:
            if len(self.path) > 3:
                if self.path[-3:] == ".py":
                    if "/" in self.path:
                        path_list = self.path.split("/")
                        path_dir = self.path.replace(path_list[-1], "")
                        self.TestSuits = seldomTestLoader.discover(path_dir, pattern=path_list[-1])
                    else:
                        # 当前目录下，和self.path有关的名字的文件中搜索
                        self.TestSuits = seldomTestLoader.discover(os.getcwd(), pattern=self.path)
                else:
                    self.TestSuits = seldomTestLoader.discover(self.path)
            else:
                self.TestSuits = seldomTestLoader.discover(self.path)

        if auto is True:
            self.run(self.TestSuits)

        # ----- Close browser globally -----
        # 全局关闭浏览器
        self.close_browser()

    def run(self, suits):
        """
        run test case
        运行测试用例
        """
        if self.debug is False:
            # 循环文件夹，查看是否有reports，没有则创建
            for filename in os.listdir(os.getcwd()):
                if filename == "reports":
                    break
            else:
                os.mkdir(os.path.join(os.getcwd(), "reports"))

            if (self.report is None) and (BrowserConfig.REPORT_PATH is not None):
                report_path = BrowserConfig.REPORT_PATH
            else:
                report_path = BrowserConfig.REPORT_PATH = os.path.join(os.getcwd(), "reports", self.report)

            with(open(report_path, 'wb')) as fp:
                if report_path.split(".")[-1] == "xml":
                    runner = XMLTestRunner(output=fp)
                    runner.run(suits)
                else:
                    runner = HTMLTestRunner(stream=fp, title=self.title, tester=self.tester,
                                            description=self.description,
                                            language=self.language, blacklist=self.blacklist, whitelist=self.whitelist)
                    # rerun:重新运行次数
                    # save_last_run:设置只保存最后一次的结果，默认为False
                    runner.run(suits, rerun=self.rerun, save_last_run=self.save_last_run)

            log.printf("generated html file: file:///{}".format(report_path))
            log.printf("generated log file: file:///{}".format(BrowserConfig.LOG_PATH))
            webbrowser.open_new("file:///{}".format(report_path))
        else:
            runner = DebugTestRunner(
                blacklist=self.blacklist,
                whitelist=self.whitelist,
                verbosity=2)
            runner.run(suits)
            log.printf("A run the test in debug mode without generating HTML report!")

    def open_browser(self):
        """
        如果browser浏览器有选择，那么打开一个监控
        If you set up a browser, open the browser
        """
        if self.browser is not None:
            log.info("存在browser")
            BrowserConfig.NAME = self.browser
            SeldomConfig.driver = Browser(BrowserConfig.NAME)
            log.info("open_browser——success")

    @staticmethod
    def close_browser():
        """
        How to open the browser, close the browser
        """
        if isinstance(SeldomConfig.driver, SeleniumWebDriver):
            SeldomConfig.driver.quit()
            SeldomConfig.driver = None


class TestMainExtend(TestMain):
    """
    TestMain tests class extensions.
    1. Collect use case information and return to the list
    2. Execute the use cases based on the use case list
    TestMain 测试类扩展。
     1.收集用例信息并返回列表
     2.根据用例列表执行用例
    """

    def __init__(self, path=None, browser=None, base_url=None, debug=False, timeout=10,
                 report=None, title="Seldom Test Report", description="Test case execution",
                 rerun=0, save_last_run=False, whitelist=[], blacklist=[], auto=False):

        if path is None:
            raise FileNotFoundError("Specify a file path—————“指定文件路径”")

        super().__init__(path=path, browser=browser, base_url=base_url, debug=debug, timeout=timeout,
                         report=report, title=title, description=description,
                         rerun=rerun, save_last_run=save_last_run, whitelist=whitelist, blacklist=blacklist,
                         auto=auto)

    @staticmethod
    def collect_cases(json=False):
        """
        返回收集到的案例信息。
        Return the collected case information.
        SeldomTestLoader.collectCaseInfo = True
        """
        if json is True:
            return sys_json.dumps(seldomTestLoader.collectCaseList)
        return seldomTestLoader.collectCaseList

    @staticmethod
    def _diff_case(file_name: str, class_name: str, method_name: str, data: list) -> bool:
        """
        Diff use case information
        差异用例信息
        :param file_name:
        :param class_name:
        :param method_name:
        :param data:
        :return:
        """
        for d in data:
            d_file = d.get("file", None)
            d_class = d.get("class").get("name", None)
            d_method = d.get("method").get("name", None)
            if (d_file is None) or (d_class is None) or (d_method is None):
                raise SeldomException(
                    """Use case format error, please refer to(用例格式错误，请参考): 
                    https://github.com/SeldomQA/seldom/blob/master/docs/platform.md""")
            if file_name == d_file and class_name == d_class and method_name == d_method:
                return True

        return False

    def run_cases(self, data: list) -> None:
        """
        运行列表案例
        run list case
        :param data:
        :return:
        """
        if isinstance(data, list) is False:
            raise TypeError("Use cases must be lists.")

        if len(data) == 0:
            log.error("There are no use cases to execute")
            return

        suit = unittest.TestSuite()
        for suits in self.TestSuits:
            for cases in suits:
                for case in cases:
                    # 获取当前case的所属模块名
                    file_name = case.__module__
                    # 获取当前类名
                    class_name = case.__class__.__name__
                    method_name = str(case).split(" ")[0]
                    ret = self._diff_case(file_name, class_name, method_name, data)
                    if ret is True:
                        suit.addTest(case)

        self.run(suit)
        self.close_browser()


main = TestMain

if __name__ == '__main__':
    main()
