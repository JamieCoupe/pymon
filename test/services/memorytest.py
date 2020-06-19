import unittest

from src.services.memory import get_virtual_memory
from src.services.memory import get_swap_memory


class MemoryInfoCase(unittest.TestCase):

    # Virtual Memory
    def test_get_virtual_memory_returns_dict(self):
        self.assertTrue(type(get_virtual_memory()) is dict)

    def test_get_virtual_memory_has_total_key(self):
        self.assertTrue('total' in get_virtual_memory())

    def test_get_virtual_memory_has_available_key(self):
        self.assertTrue('available' in get_virtual_memory())

    def test_get_virtual_memory_has_used_key(self):
        self.assertTrue('used' in get_virtual_memory())

    def test_get_virtual_memory_has_percentage_key(self):
        self.assertTrue('percentage' in get_virtual_memory())

    def test_get_virtual_memory_total_not_0(self):
        self.assertTrue(get_virtual_memory()['total'] != 0)

    def test_get_virtual_memory_available_not_0(self):
        self.assertTrue(get_virtual_memory()['available'] != 0)

    def test_get_virtual_memory_used_not_0(self):
        self.assertTrue(get_virtual_memory()['used'] != 0)

    def test_get_virtual_memory_percentage_not_0(self):
        self.assertTrue(get_virtual_memory()['percentage'] != 0)


    # Swap Memory
    def test_get_swap_memory_returns_dict(self):
        self.assertTrue(type(get_swap_memory()) is dict)

    def test_get_swap_memory_has_total_key(self):
        self.assertTrue('total' in get_swap_memory())

    def test_get_swap_memory_has_available_key(self):
        self.assertTrue('available' in get_swap_memory())

    def test_get_swap_memory_has_used_key(self):
        self.assertTrue('used' in get_swap_memory())

    def test_get_swap_memory_has_percentage_key(self):
        self.assertTrue('percentage' in get_swap_memory())

    def test_get_swap_memory_total_not_0(self):
        self.assertTrue(get_swap_memory()['total'] != 0)

    def test_get_swap_memory_available_not_0(self):
        self.assertTrue(get_swap_memory()['available'] != 0)

    def test_get_swap_memory_used_not_0(self):
        self.assertTrue(get_swap_memory()['used'] != 0)

    def test_get_swap_memory_percentage_not_0(self):
        self.assertTrue(get_swap_memory()['percentage'] != 0)


if __name__ == '__main__':
    unittest.main()
