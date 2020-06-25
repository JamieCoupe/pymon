import unittest
from src.services.gpu import get_nvidia_gpu_data


def list_subkey_lister(input_list):
    subkeys = []
    for v in input_list:
        if type(v) is dict:
            for k1, v1 in v.items():
                subkeys.append(k1)
        else:
            continue

    return subkeys


class TestGpuCase(unittest.TestCase):
    def test_get_nvidia_gpu_data_returns_list(self):
        self.assertTrue(list, type(get_nvidia_gpu_data))

    def test_get_nvidia_gpu_data_returns_at_least_eight_bits_of_data(self):
        self.assertEquals(8, len(get_nvidia_gpu_data()))


if __name__ == '__main__':
    unittest.main()
