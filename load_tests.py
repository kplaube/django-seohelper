#!/usr/bin/env python
import sys
from unittest import TestSuite
from boot_django import boot_django

boot_django()

default_labels = ["seohelper.tests", ]


def get_suite(labels=default_labels):
    from django.test.runner import DiscoverRunner

    runner = DiscoverRunner(verbosity=1)
    failures = runner.run_tests(labels)
    if failures:
        sys.exit(failures)

    # In case this is called from setuptools, return a test suite
    return TestSuite()


if __name__ == "__main__":
    command_line_labels = sys.argv[1:]
    labels = command_line_labels if command_line_labels else default_labels
    get_suite(labels)
