# _*_ coding:utf-8 _*_

import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from Common_Function import HTMLTestReportCN
from Common_Function.readConfig import ReadConfig
from Common_Function.caseStrategy import CaseStrategy


class RunAllTests(object):

    def __init__(self):
        cs = CaseStrategy()
        self.test_suite = cs.collect_cases()
        self.tester = ReadConfig().get_test_account()['name']

    def run(self):
        # 启动测试时创建文件夹并获取报告的名字
        daf = HTMLTestReportCN.DirAndFiles()
        daf.create_dir(title='CDS测试报告')
        report_path = HTMLTestReportCN.GlobalMsg.get_value("report_path")

        with open(report_path, "wb") as fp:
            runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title='CDS测试报告', description='用例执行情况：',
                                                     tester=self.tester)
            runner.run(self.test_suite)


if __name__ == "__main__":
    RunAllTests().run()
