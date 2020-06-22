import unittest

from datetime import datetime
from src.services.process import get_processes_info
from src.services.process import get_create_time
from src.services.process import get_random_process
from src.services.process import get_number_of_cores
from src.services.process import get_process_priority
from src.services.process import get_process_memory_usage
from src.services.process import get_process_io
from src.services.process import get_cpu_usage
from src.services.process import get_process_threads
from src.services.process import get_process_username


def list_subkey_lister(input_list):
    subkeys = []
    for v in input_list:
        if type(v) is dict:
            for k1, v1 in v.items():
                subkeys.append(k1)
        else:
            continue

    return subkeys


class ProcessTestCase(unittest.TestCase):

    process = ''

    def setUp(self):
        global process
        process = get_random_process()

    # Process Information
    def test_get_processes_info_returns_list(self):
        self.assertTrue(type(get_processes_info()) is list)

    def test_get_processes_info_has_pid_key(self):
        self.assertTrue('pid' in list_subkey_lister(get_processes_info()))

    def test_get_processes_info_has_name_key(self):
        self.assertTrue('name' in list_subkey_lister(get_processes_info()))

    def test_get_processes_info_has_create_time_key(self):
        self.assertTrue('create_time' in list_subkey_lister(get_processes_info()))

    def test_get_processes_info_has_cores_key(self):
        self.assertTrue('cores' in list_subkey_lister(get_processes_info()))

    def test_get_processes_info_has_cpu_usage_key(self):
        self.assertTrue('cpu_usage' in list_subkey_lister(get_processes_info()))

    def test_get_processes_info_has_status_key(self):
        self.assertTrue('status' in list_subkey_lister(get_processes_info()))

    def test_get_processes_info_has_nice_key(self):
        self.assertTrue('nice' in list_subkey_lister(get_processes_info()))

    def test_get_processes_info_has_memory_usage_key(self):
        self.assertTrue('memory_usage' in list_subkey_lister(get_processes_info()))

    def test_get_processes_info_has_n_threads_key(self):
        self.assertTrue('n_threads' in list_subkey_lister(get_processes_info()))

    # Sub process information methods
    def test_get_create_time_returns_time(self):
        self.assertTrue(type(get_create_time(process)) is datetime)

    def test_get_number_of_cores_returns_number(self):
        self.assertTrue(type(get_number_of_cores(process)) is int)

    def test_get_cpu_usage_returns_number_or_na(self):
        self.assertTrue(type(get_cpu_usage(process)) is float or get_cpu_usage(process) == "N/A")

    def test_get_cpu_usage_is_greater_or_equal_than_zero(self):
        if type(get_cpu_usage(process)) is float:

            self.assertTrue(get_cpu_usage(process) >= 0.0)
        else:
            self.assertTrue(get_cpu_usage(process) == "N/A")

    def test_get_cpu_usage_less_than_equal_to_100(self):
        if type(get_cpu_usage(process)) is float:

            self.assertTrue(get_cpu_usage(process) <= 100.0)
        else:
            self.assertTrue(get_cpu_usage(process) == "N/A")

    def test_get_process_priority_returns_number(self):
        self.assertTrue(type(get_process_priority(process) is int))

    def test_get_process_priority_returns_number_from_0_to_139(self):
        self.assertTrue(get_process_priority(process) in range(139))

    def test_get_process_memory_usage_returns_number(self):
        self.assertTrue(type(get_process_memory_usage(process)) is int)

    def test_get_process_memory_usage_returns_value_between_0_and_68719476736(self):
        self.assertTrue(get_process_memory_usage(process) in range(68719476736))

    def test_get_process_threads_returns_number(self):
        self.assertTrue(type(get_process_threads(process)) is int)

    def test_get_process_threads_returns_more_than_0(self):
        self.assertTrue(get_process_threads(process) >= 0)

    def test_get_process_threads_returns_less_than_16(self):
        self.assertTrue(type(get_process_threads(process) <= 100))

    def test_get_process_username_returns_string(self):
        self.assertTrue(type(get_process_username(process)) is str)

    def test_get_process_username_returns_not_empty_string(self):
        self.assertTrue(len(get_process_username(process)) > 0 )
        self.assertTrue(get_process_username(process) is not None)

    def test_get_process_username_returns_less_than_200_characters(self):
        self.assertTrue(len(get_process_username(process)) < 200)

    def test_get_process_io_returns_dict(self):
        self.assertTrue(type(get_process_io(process)) is dict)

    def test_get_process_io_has_read_bytes_key(self):
        self.assertTrue('read_bytes' in get_process_io(process))

    def test_get_process_io_has_write_bytes_key(self):
        self.assertTrue('write_bytes' in get_process_io(process))


if __name__ == '__main__':
    unittest.main()
