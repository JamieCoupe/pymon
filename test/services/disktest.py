import unittest

from src.services.disk import get_disk_partitions_and_usage
from src.services.disk import get_disk_io


def dictonary_subkey_lister(dictonary):
    subkeys = []
    for k, v in dictonary.items():
        for k1, v1 in v.items():
            subkeys.append(k1)
            if type(v1) is dict:
                for k2, v2 in v1.items():
                    subkeys.append(k2)
            else:
                continue

    print(subkeys)

    return subkeys


class DiskTestCase(unittest.TestCase):

    # Disk and partitions
    def test_get_disk_partition_and_usage_returns_dict(self):
        self.assertTrue(type(get_disk_partitions_and_usage()) is dict)

    def test_get_disk_partition_and_usage_has_mountpoint_key(self):
        self.assertTrue('mountpoint' in dictonary_subkey_lister(get_disk_partitions_and_usage()))

    def test_get_disk_partition_and_usage_has_fs_type_key(self):
        self.assertTrue('fs_type' in dictonary_subkey_lister(get_disk_partitions_and_usage()))

    def test_get_disk_partition_and_usage_has_usage_key(self):
        self.assertTrue('usage' in dictonary_subkey_lister(get_disk_partitions_and_usage()))

    def test_get_disk_partition_and_usage_has_total_key(self):
        self.assertTrue('total' in dictonary_subkey_lister(get_disk_partitions_and_usage()))

    def test_get_disk_partition_and_usage_has_available_key(self):
        self.assertTrue('available' in dictonary_subkey_lister(get_disk_partitions_and_usage()))

    def test_get_disk_partition_and_usage_has_used_key(self):
        self.assertTrue('used' in dictonary_subkey_lister(get_disk_partitions_and_usage()))

    def test_get_disk_partition_and_usage_has_percentage_key(self):
        self.assertTrue('percentage' in dictonary_subkey_lister(get_disk_partitions_and_usage()))

    # IO
    def test_get_disk_io_returns_not_none(self):
        self.assertTrue(get_disk_io() is not None)

    def test_get_disk_io_returns_dict(self):
        self.assertTrue(type(get_disk_io())is dict)

    def test_get_disk_io_has_read_key(self):
        self.assertTrue('read' in get_disk_io())

    def test_get_disk_io_has_write_key(self):
        self.assertTrue('write' in get_disk_io())

    def test_get_disk_io_read_value_not_zero(self):
        self.assertFalse(get_disk_io()['read'] == 0)

    def test_get_disk_io_write_value_not_zero(self):
        self.assertFalse(get_disk_io()['write'] == 0)


if __name__ == '__main__':
    unittest.main()
