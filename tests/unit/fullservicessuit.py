import unittest
from tests.unit.services.cpu_test import TestCpuInfoCase
from tests.unit.services.sysinfo_test import TestSysInfoCase
from tests.unit.services.memory_test import TestMemoryInfoCase
from tests.unit.services.disk_test import TestDiskCase
from tests.unit.services.utilities_test import TestUtilitiesCase
from tests.unit.services.network_test import TestNetworkCase
from tests.unit.services.process_test import TestProcessCase


def run_suite():
    # Run only the tests in the specified classes

    test_classes_to_run = [TestCpuInfoCase, TestSysInfoCase, TestMemoryInfoCase, TestDiskCase, TestUtilitiesCase,
                           TestNetworkCase, TestProcessCase]

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
