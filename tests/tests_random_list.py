import unittest

from random_list import RandomList


class TestRandomList(unittest.TestCase):
    def test_constructor(self):
        # Given
        n = 10
        # When
        result_list = RandomList(n)
        # Then
        self.assertEqual(len(result_list), n)
        self.assertEqual(all(v is not None for v in result_list), True)

    def test_sort_list(self):
        # Given
        n = 10
        # When & Then
        unsorted_list = RandomList(n)
        self.assertFalse(all(unsorted_list[i] <= unsorted_list[i + 1] for i in range(len(unsorted_list) - 1)))
        sorted_list = unsorted_list.sort_list()
        self.assertTrue(all(sorted_list[i] <= sorted_list[i + 1] for i in range(len(sorted_list) - 1)))
