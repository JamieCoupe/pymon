import unittest
from tests.unit.services.cpu_test import CpuInfoCase
from tests.unit.services.sysinfo_test import SysInfoCase
from tests.unit.services.memory_test import MemoryInfoCase
from tests.unit.services.disk_test import DiskTestCase
from tests.unit.services.utilities_test import UtilitiesTestCase
from tests.unit.services.network_test import NetworkTestCase
from tests.unit.services.process_test import ProcessTestCase


def run_suite():
    # Run only the tests in the specified classes

    test_classes_to_run = [CpuInfoCase, SysInfoCase, MemoryInfoCase, DiskTestCase, UtilitiesTestCase,
                           NetworkTestCase, ProcessTestCase]

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
