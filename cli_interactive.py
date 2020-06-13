#!/usr/bin/env python3

from __future__ import print_function, unicode_literals

from PyInquirer import prompt

from test_runner import TestRunner
from tests.examples import TestExamples
from utils.config import Config
from utils.language import Language


def execute_on_answers(answers, language):
    try:
        if answers['section'] == language._("trivial"):
            TestExamples.trivial_example()
        if answers['section'] == language._("complex"):
            TestExamples.complex_example()
        elif answers['section'] == language._("summary"):
            TestRunner.run_test_summary_suite()
    except AssertionError:
        pass
    if answers['section'] == language._("exit"):
        exit(0)


def main():
    language = Language(Config())
    questions = [
        {
            'type': 'list',
            'name': 'section',
            'message': language._("hello"),
            'choices': [
                language._("trivial"),
                language._("complex"),
                language._("summary"),
                language._("exit"),
            ]
        }
    ]
    answers = prompt(questions)
    execute_on_answers(answers, language)

    main()


if __name__ == "__main__":
    main()
