import os
import unittest


class CaseStrategy:
    def __init__(self):
        self.suite_path = 'test_suites'
        self.case_path = 'test_XPS'
        self.case_pattern = 'test_*.py'

    def _collect_cases(self, start, cases, top_dir=None):
        # 批量跑用例
        suites = unittest.defaultTestLoader.discover(start_dir=start,
                                                     pattern=self.case_pattern, top_level_dir=top_dir)
        # print("suites::::{0}".format(suites))
        # < unittest.suite.TestSuite tests = [ < unittest.suite.TestSuite tests = [] >, < unittest.suite.TestSuite tests = [ < unittest.suite.TestSuite
        # tests = [ < test_CDS.test_01_index.Index testMethod = test_01_login >] >] >] >

        for suite in suites:
            # print("suite::::{0}".format(suite))
            for case in suite:
                # print("case::::{0}".format(case))
                cases.addTest(case)

    def collect_cases(self, suite=True):
        """collect cases

        collect cases from the giving path by case_path via the giving pattern by case_pattern

        return: all cases that collected by the giving path and pattern, it is a unittest.TestSuite()

        """
        cases = unittest.TestSuite()

        if suite:
            test_suites = []
            project_dir = os.path.dirname(os.path.dirname(__file__))
            # 返回指定的文件夹包含的文件或文件夹的名字的列表

            for file in os.listdir(project_dir):
                if self.suite_path in file:
                    suites_dir = os.path.join(project_dir, file)
                    if os.path.isdir(suites_dir):
                        test_suites.append(suites_dir)
            for test_suite in test_suites:
                for file in os.listdir(os.path.join(test_suite, self.case_path)):
                    if file[-2:] != 'py' and file[-2:] != '__':
                        # print("++++++++++++{0}".format(file))
                        # print(os.path.join(test_suite, self.case_path))
                        self._collect_cases(file, cases, top_dir=os.path.join(test_suite, self.case_path))
        else:
            self._collect_cases(self.case_path, cases, top_dir=None)

        return cases
