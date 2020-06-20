import unittest
from tests.unit.services.cputest import CpuInfoCase
from tests.unit.services.sysinfotest import SysInfoCase
from tests.unit.services.memorytest import MemoryInfoCase
from tests.unit.services.disktest import DiskTestCase
from tests.unit.services.utilitiestest import UtilitiesTestCase
from tests.unit.services.networktest import NetworkTestCase


def run_suite():
    # Run only the tests in the specified classes

    test_classes_to_run = [CpuInfoCase, SysInfoCase, MemoryInfoCase, DiskTestCase, UtilitiesTestCase,
                           NetworkTestCase]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    full_service_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(full_service_suite)


if __name__ == '__main__':
    run_suite()
