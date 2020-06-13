import unittest
from collections import namedtuple
from unittest import mock
from unittest.mock import patch, PropertyMock

from utils.singleton import Singleton
from utils.language import Language


class TestLanguage(unittest.TestCase):
    def setUp(self):
        Singleton._instances = {}

    def tearDown(self):
        Singleton._instances = {}

    def tests_create_language(self):
        # Given
        Language.language_dict = {'PL': {}}
        config = namedtuple('MockedConfig', 'language')('PL')
        # When
        language_object = Language(config)
        # Then
        self.assertEqual(language_object.language, config.language)

    @patch('utils.language.Language.set_language_dict')
    def tests_create_language_not_supported(self, mock_set_language):
        # Given
        language_dict = {'EN': {}}
        mock_set_language.return_value = language_dict
        config = namedtuple('MockedConfig', 'language')('PL')
        # When & Then
        with self.assertRaises(AssertionError):
            Language(config)

    @patch('utils.language.Language.set_language_dict')
    def tests_get_section_text(self, mock_set_language):
        # Given
        language_dict = {'EN': {'section_a': 0, 'section_b': 10, 'translation_not_found': None}}
        mock_set_language.return_value = language_dict
        config = namedtuple('MockedConfig', 'language')('EN')
        # When
        language = Language(config)
        # Then
        self.assertEqual(language_dict['EN']['section_a'], language._('section_a'))
        self.assertEqual(language_dict['EN']['section_b'], language._('section_b'))
        with self.assertRaises(AssertionError):
            language._('section_c')
