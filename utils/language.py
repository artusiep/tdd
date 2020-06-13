from utils.singleton import Singleton


class Language(metaclass=Singleton):
    def __init__(self, config):
        self.language_dict = self.set_language_dict()
        self.__is_supported_language(config.language)
        self.language = config.language

    @staticmethod
    def set_language_dict():
        return {
            'PL': {
                'hello': 'Test Runner TiWO etap2',
                'translation_not_found': 'Nie znaleziono tłumaczenia',
                'trivial': 'Prosty (trywialny) przykład, pokazujący działanie',
                'complex': 'Przykład bardziej skomplikowany (zaawansowany)',
                'summary': 'Podsumowanie uruchomienia testów',
                'exit': 'Powrót do systemu',
                'list_generation_result': 'Wygenerowano listę: {}',
                'start_sorting_info': 'Sortowanie rozpoczęte',
                'list_sorting_result': 'Efekt sortowania: {}'
            },
            'EN': {
                'hello': 'Test Runner TiWO stage 2',
                'translation_not_found': 'Translation not found',
                'trivial': 'Simple (trivial) example showing usage of program',
                'complex': 'More complex example',
                'summary': 'Summary of running tests',
                'exit': 'Exit to system',
                'list_generation_result': 'Generated list: {}',
                'start_sorting_info': 'Sorting started',
                'list_sorting_result': 'Sorting result: {}'
            }
        }

    def __is_supported_language(self, language):
        assert language in self.language_dict, f'Language is not supported. Supported Languages {list(self.language_dict.keys())}'

    # noinspection PyPropertyDefinition
    def _(self, section) -> str:
        assert section in self.language_dict[self.language], self.language_dict[self.language]['translation_not_found']
        return self.language_dict[self.language][section]
