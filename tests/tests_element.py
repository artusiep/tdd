import unittest

from element import Element


class TestElement(unittest.TestCase):
    def test_equality(self):
        # Given
        element1 = Element(1)
        element2 = Element(1)
        # When & Then
        self.assertEqual(element1, element2)

    def test_gt(self):
        # Given
        element1 = Element(5)
        element2 = Element(0)
        # When & Then
        self.assertGreater(element1, element2)

    def test_ge(self):
        # Given
        element1 = Element(0)
        element2 = Element(0)
        # When & Then
        self.assertGreaterEqual(element1, element2)