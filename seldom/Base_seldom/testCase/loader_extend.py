"""seldom Loading unittests."""
"""加载单元测试"""
import functools
from fnmatch import fnmatchcase
from unittest.loader import TestLoader


class SeldomTestLoader(TestLoader):
    """
    This class is responsible for loading tests according to various criteria
    and returning them wrapped in a TestSuite
    此类负责根据各种标准加载测试并将它们包装在 TestSuite 中返回
    """
    testNamePatterns = None
    collectCaseInfo = False  # Switch of collecting use case information:收集用例信息的开关
    collectCaseList = []  # List of use case information:用例信息列表

    def getTestCaseNames(self, testCaseClass):
        """
        Return a sorted sequence of method names found within testCaseClass
        返回在 testCaseClass 中找到的方法名称的排序序列
        """

        def shouldIncludeMethod(attrname):
            if not attrname.startswith(self.testMethodPrefix):
                return False
            testFunc = getattr(testCaseClass, attrname)
            if not callable(testFunc):
                return False
            fullName = f'%s.%s.%s' % (
                testCaseClass.__module__, testCaseClass.__qualname__, attrname
            )
            if self.collectCaseInfo is True:
                case_info = {
                    "file": testCaseClass.__module__,
                    "class": {
                        "name": testCaseClass.__name__,
                        "doc": testCaseClass.__doc__
                    },
                    "method": {
                        "name": attrname,
                        "doc": testFunc.__doc__
                    }
                }
                self.collectCaseList.append(case_info)

            return self.testNamePatterns is None or \
                   any(fnmatchcase(fullName, pattern) for pattern in self.testNamePatterns)

        testFnNames = list(filter(shouldIncludeMethod, dir(testCaseClass)))
        if self.sortTestMethodsUsing:
            testFnNames.sort(key=functools.cmp_to_key(self.sortTestMethodsUsing))
        return testFnNames


seldomTestLoader = SeldomTestLoader()
