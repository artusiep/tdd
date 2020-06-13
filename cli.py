#!/usr/bin/env python3

import argparse
import json

from tests.examples import TestExamples
from test_runner import TestRunner
from utils.config import Config
from utils.language import Language


def main():
    language = Language(Config())
    parser = argparse.ArgumentParser(description=language._('hello'))
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--trivial', help=language._('trivial'), action="store_true")
    group.add_argument('-c', '--complex', help=language._('complex'), action="store_true")
    group.add_argument('-s', '--summary', help=language._('summary'), action="store_true")
    args = parser.parse_args()

    if args.trivial:
        TestExamples.trivial_example()
    elif args.complex:
        TestExamples.complex_example()
    elif args.summary:
        TestRunner.run_test_summary_suite()


if __name__ == "__main__":
    main()
