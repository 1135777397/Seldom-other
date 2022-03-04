import os
import unittest


class CaseStrategy:
	def __init__(self):
		self.suite_path = 'test_suites'
		self.case_path = 'test_CDS'
		self.case_pattern = 'test_*.py'

	def _collect_cases(self, cases, top_dir=None):
		# 批量跑用例
		suites = unittest.defaultTestLoader.discover(self.case_path,
													 pattern=self.case_pattern, top_level_dir=top_dir)
		for suite in suites:
			for case in suite:
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
					suites_dir = os.path.join(project_dir,file)
					if os.path.isdir(suites_dir):
						# 如果存在文件夹，则把文件夹名存到test_suites中
						test_suites.append(suites_dir)
			for test_suite in test_suites:
				self._collect_cases(cases, top_dir=test_suite)
		else:
			self._collect_cases(cases, top_dir=None)

		return cases
