import unittest
from src.services.cpu import get_static_info
from src.services.cpu import get_current_frequency
from src.services.cpu import get_usage_per_core
from src.services.cpu import get_total_cpu_usage


class CpuInfoCase(unittest.TestCase):

    def test_get_static_info_returns_dict(self):
        self.assertTrue(type(get_static_info()) is dict)

    def test_current_frequency_greater_than_1000_Mhz(self):
        self.assertGreater(get_current_frequency(), 1000)

    # Only tests 4 cores (Could have multiple cores with 4 likely being the lowest)
    def test_usage_per_core_first_core_greater_than_0(self):
        self.assertGreater(get_usage_per_core()[0], 0)

    def test_usage_per_core_second_core_greater_than_0(self):
        self.assertGreater(get_usage_per_core()[1], 0)

    def test_usage_per_core_third_core_greater_than_0(self):
        self.assertGreater(get_usage_per_core()[2], 0)

    def test_usage_per_core_fourth_core_greater_than_0(self):
        self.assertGreater(get_usage_per_core()[3], 0)

    # Get total CPU usage %
    def test_total_cpu_usage_greater_than_0(self):
        print(get_total_cpu_usage())
        self.assertNotEqual(get_total_cpu_usage(), 0)


if __name__ == '__main__':
    unittest.main()
