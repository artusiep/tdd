import unittest

from tests.tests_element import TestElement
from tests.tests_language import TestLanguage
from tests.tests_random_list import TestRandomList


class TestRunner:
    @staticmethod
    def run_test_summary_suite():
        test_cases = [TestElement, TestLanguage, TestRandomList]
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        for test_class in test_cases:
            tests = loader.loadTestsFromTestCase(test_class)
            suite.addTests(tests)
        return TestRunner.run_suite(suite)

    @staticmethod
    def run_suite(suite):
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
