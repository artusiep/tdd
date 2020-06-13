import unittest

from random_list import RandomList
from test_runner import TestRunner
from utils.config import Config
from utils.language import Language


class TestExamples(unittest.TestCase):

    def test_trivial(self):
        # Given
        n = 3
        # When & Then
        unsorted_list = RandomList(n)
        print()
        print(Language(Config())._('list_generation_result').format(unsorted_list))
        print(Language(Config())._('start_sorting_info'))
        sorted_list = unsorted_list.sort_list()
        print(Language(Config())._('list_sorting_result').format(str(sorted_list)))
        self.assertTrue(all(sorted_list[i] <= sorted_list[i + 1] for i in range(len(sorted_list) - 1)))

    def test_complex(self):
        # Given
        n = 100
        # When & Then
        unsorted_list = RandomList(n)
        print()
        print(Language(Config())._('list_generation_result').format(unsorted_list))
        print(Language(Config())._('start_sorting_info'))
        self.assertFalse(all(unsorted_list[i] <= unsorted_list[i + 1] for i in range(len(unsorted_list) - 1)))
        sorted_list = unsorted_list.sort_list()
        print(Language(Config())._('list_sorting_result').format(str(sorted_list)))
        self.assertTrue(all(sorted_list[i] <= sorted_list[i + 1] for i in range(len(sorted_list) - 1)))


    @staticmethod
    def trivial_example():
        suite = unittest.TestSuite()
        suite.addTest(TestExamples('test_trivial'))
        TestRunner.run_suite(suite)

    @staticmethod
    def complex_example():
        suite = unittest.TestSuite()
        suite.addTest(TestExamples('test_complex'))
        TestRunner.run_suite(suite)

