import unittest
import os
import pandas

from datetime import datetime
from pymoncore.services import get_all_processes_info
from pymoncore.services import get_process_create_time
from pymoncore.services import get_random_process
from pymoncore.services import get_process_core_usage
from pymoncore.services import get_process_priority
from pymoncore.services import get_process_memory_usage
from pymoncore.services import get_process_io
from pymoncore.services import get_process_cpu_usage
from pymoncore.services import get_process_threads
from pymoncore.services import get_process_username
from pymoncore.services import get_process_name
from pymoncore.services import get_process_status
from pymoncore.services import construct_dataframe


def list_subkey_lister(input_list):
    subkeys = []
    for v in input_list:
        if type(v) is dict:
            for k1, v1 in v.items():
                subkeys.append(k1)
        else:
            continue

    return subkeys


class TestProcessCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.process = get_random_process()
        cls.priority = get_process_priority(cls.process)
        cls.process_name = get_process_name(cls.process)
        cls.process_cores = get_process_core_usage(cls.process)
        cls.process_cpu_usage = get_process_cpu_usage(cls.process)
        cls.process_status = get_process_status(cls.process)
        cls.process_priority = get_process_priority(cls.process)
        cls.process_memory_usage = get_process_memory_usage(cls.process)
        cls.process_threads = get_process_threads(cls.process)
        cls.process_username = get_process_username(cls.process)
        cls.process_io = get_process_io(cls.process)
        cls.processes_info = get_all_processes_info()
        cls.processes = get_all_processes_info()
        cls.process_dataframe = construct_dataframe(cls.processes_info, "memory_usage", "name,memory_usage",
                                                    descending=False)

    # Process Information
    def test_get_processes_info_returns_list(self):
        self.assertTrue(type(self.processes_info) is list)

    def test_get_processes_info_has_pid_key(self):
        self.assertTrue('pid' in list_subkey_lister(self.processes_info))

    def test_get_processes_info_has_name_key(self):
        self.assertTrue('name' in list_subkey_lister(self.processes_info))

    def test_get_processes_info_has_create_time_key(self):
        self.assertTrue('create_time' in list_subkey_lister(self.processes_info))

    def test_get_processes_info_has_cores_key(self):
        self.assertTrue('cores' in list_subkey_lister(self.processes_info))

    def test_get_processes_info_has_cpu_usage_key(self):
        self.assertTrue('cpu_usage' in list_subkey_lister(self.processes_info))

    def test_get_processes_info_has_status_key(self):
        self.assertTrue('status' in list_subkey_lister(self.processes_info))

    def test_get_processes_info_has_nice_key(self):
        self.assertTrue('nice' in list_subkey_lister(self.processes_info))

    def test_get_processes_info_has_memory_usage_key(self):
        self.assertTrue('memory_usage' in list_subkey_lister(self.processes_info))

    def test_get_processes_info_has_n_threads_key(self):
        self.assertTrue('n_threads' in list_subkey_lister(self.processes_info))

    def test_get_processes_info_has_read_bytes_key(self):
        self.assertTrue('read_bytes' in list_subkey_lister(self.processes_info))

    def test_get_processes_info_has_write_bytes_key(self):
        self.assertTrue('write_bytes' in list_subkey_lister(self.processes_info))

    # Sub process information methodstest_get_process_name_returns_non_empty_string
    def test_get_process_name_returns_string(self):
        self.assertTrue(type(self.process_name) is str)

    def test_get_process_name_returns_non_empty_string(self):
        self.assertTrue(self.process_name != "")
        self.assertTrue(self.process_name is not None)

    def test_get_process_create_time_returns_time(self):
        self.assertTrue(type(get_process_create_time(self.process)) is datetime)

    def test_get_process_number_of_cores_returns_number(self):
        self.assertTrue(type(self.process_cores) is int or self.process_cores in ["AccessDenied", "Not On Platform"])

    def test_get_process_cpu_usage_returns_number_or_na_or_unavailable(self):
        self.assertTrue(type(self.process_cpu_usage) is float or self.process_cpu_usage in ["AccessDenied",                                                                                  "Not On Platform"])

    def test_get_process_cpu_usage_is_greater_or_equal_than_zero(self):
        if type(self.process_cpu_usage) is float:
            self.assertTrue(self.process_cpu_usage >= 0.0)
        else:
            self.assertTrue(self.process_cpu_usage == "AccessDenied")

    def test_get_process_cpu_usage_less_than_equal_to_100(self):
        if type(self.process_cpu_usage) is float:
            self.assertTrue(self.process_cpu_usage <= 100.0)
        else:
            self.assertTrue(self.process_cpu_usage == "AccessDenied")

    def test_get_process_status_returns_string(self):
        self.assertTrue(type(self.process_name) is str)

    def test_get_process_status_returns_valid_status(self):
        self.assertTrue(self.process_status in ["AccessDenied", "running", "stopped", "paused"])

    def test_get_process_priority_returns_number_or_access_denied(self):
        self.assertTrue(type(self.priority) is int or self.priority == "AccessDenied")

    def test_get_process_priority_returns_number_from_0_to_139(self):
        if type(self.priority) is int:
            self.assertTrue(self.priority in range(139))
        else:
            self.assertTrue(self.priority == "AccessDenied")

    def test_get_process_memory_usage_returns_number(self):
        self.assertTrue(type(self.process_memory_usage) is int)

    def test_get_process_memory_usage_returns_value_between_0_and_68719476736(self):
        if 'nt' not in os.name:
            self.skipTest("Doesn't Run on non windows")
        self.assertTrue(self.process_memory_usage in range(100000000))

    def test_get_process_threads_returns_number(self):
        self.assertTrue(type(self.process_threads) is int or self.process_threads == "AccessDenied")

    def test_get_process_threads_returns_more_than_0(self):
        if type(self.process_threads) is int:
            self.assertTrue(self.process_threads >= 0)
        else:
            self.assertTrue(self.process_threads == "AccessDenied")

    def test_get_process_threads_returns_less_than_16(self):
        if type(self.process_threads) is int:
            self.assertTrue(type(self.process_threads <= 100))
        else:
            self.assertTrue(self.process_threads == "AccessDenied")

    def test_get_process_username_returns_string(self):
        self.assertTrue(type(self.process_username) is str)

    def test_get_process_username_returns_not_empty_string(self):
        self.assertTrue(len(self.process_username) > 0)
        self.assertTrue(self.process_username is not None)

    def test_get_process_username_returns_less_than_200_characters(self):
        self.assertTrue(len(self.process_username) < 200)

    def test_get_process_io_returns_dict(self):
        self.assertTrue(type(self.process_io) is dict)

    def test_get_process_io_has_read_bytes_key(self):
        self.assertTrue('read_bytes' in self.process_io)

    def test_get_process_io_has_write_bytes_key(self):
        self.assertTrue('write_bytes' in self.process_io)

    # Dataframe construction
    def test_construct_dataframe_returns_a_dataframe(self):
        self.assertTrue(type(self.process_dataframe) is pandas.DataFrame)



if __name__ == '__main__':
    unittest.main()
