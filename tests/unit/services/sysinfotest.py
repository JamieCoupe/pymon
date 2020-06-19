import unittest
from src.services.sysinfo import get_sysinfo
from src.services.sysinfo import get_boot_time


class SysInfoCase(unittest.TestCase):

    def test_get_sysinfo_returns_dict(self):
        self.assertTrue(type(get_sysinfo()) is dict)

    def test_get_sysinfo_system_key_not_empty(self):
        self.assertGreater(len(get_sysinfo()['system']), 0)

    def test_get_sysinfo_node_name_key_not_empty(self):
        self.assertGreater(len(get_sysinfo()['node_name']), 0)

    def test_get_sysinfo_release_key_not_empty(self):
        self.assertGreater(len(get_sysinfo()['release']), 0)

    def test_get_sysinfo_version_key_not_empty(self):
        self.assertGreater(len(get_sysinfo()['version']), 0)

    def test_get_sysinfo_architecture_key_not_empty(self):
        self.assertGreater(len(get_sysinfo()['architecture']), 0)

    def test_get_sysinfo_processor_key_not_empty(self):
        self.assertGreater(len(get_sysinfo()['processor']), 0)

    def test_get_boot_time_returns_28_characters(self):
        # 27 for Windows 28 for Mac
        self.assertIn(len(get_boot_time()), [27, 28, 29])


if __name__ == '__main__':
    unittest.main()
