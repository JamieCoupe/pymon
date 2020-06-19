import unittest
import cputest
from .sysinfotest import SysInfoCase


def run_suite():
    # Run only the tests in the specified classes

    test_classes_to_run = [CpuInfoCase, SysInfoCase]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)


if __name__ == '__main__':
    run_suite()
