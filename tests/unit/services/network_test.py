import unittest

from pymoncore.services.network import get_network_interfaces
from pymoncore.services.network import get_network_io


def dictonary_subkey_lister(dictonary):
    subkeys = []
    for k, v in dictonary.items():
        for v1 in v:
            if type(v1) is dict:
                for k2, v2 in v1.items():
                    subkeys.append(k2)
            else:
                continue
    return subkeys


class TestNetworkCase(unittest.TestCase):

    # Network Interfaces
    def test_get_network_interface_returns_dict(self):
        self.assertTrue(type(get_network_interfaces()) is dict)

    def test_get_network_interface_has_ip_address_key(self):
        self.assertTrue('ip_address' in dictonary_subkey_lister(get_network_interfaces()))

    def test_get_network_interface_has_net_mask_key(self):
        self.assertTrue('net_mask' in dictonary_subkey_lister(get_network_interfaces()))

    def test_get_network_interface_has_ip_broadcast_key(self):
        self.assertTrue('ip_broadcast' in dictonary_subkey_lister(get_network_interfaces()))

    # IO
    def test_get_network_io_returns_not_none(self):
        self.assertTrue(get_network_io() is not None)

    def test_get_network_io_returns_dict(self):
        self.assertTrue(type(get_network_io())is dict)

    def test_get_network_io_has_read_key(self):
        self.assertTrue('sent' in get_network_io())

    def test_get_network_io_has_write_key(self):
        self.assertTrue('received' in get_network_io())

    def test_get_network_io_read_value_not_zero(self):
        self.assertFalse(get_network_io()['sent'] == 0)

    def test_get_network_io_write_value_not_zero(self):
        self.assertFalse(get_network_io()['received'] == 0)


if __name__ == '__main__':
    unittest.main()
