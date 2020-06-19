import unittest

from src.services.utilities import get_size


class UtilitiesCase(unittest.TestCase):

    def test_get_size_returns_same_when_10_entered(self):
        self.assertEqual("10.00B", get_size(10))

    def test_get_size_returns_1kb_when_1024_entered(self):
        self.assertEqual("1.00KB", get_size(1024))

    def test_get_size_returns_1Mb_when_1048576_entered(self):
        self.assertEqual("1.00MB", get_size(1048576))

    def test_get_size_returns_1Gb_when_1073741824_entered(self):
        self.assertEqual("1.00GB", get_size(1073741824))

    def test_get_size_returns_1Tb_when_1099511627776_entered(self):
        self.assertEqual("1.00TB", get_size(1099511627776))

    def test_get_size_returns_1Pb_when_1125899906842624_entered(self):
        self.assertEqual("1.00PB", get_size(1125899906842624))


if __name__ == '__main__':
    unittest.main()
