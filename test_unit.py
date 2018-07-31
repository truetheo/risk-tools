import unittest
from black_scholes import BlackScholes


class TestFactorial(unittest.TestCase):
    """
    ESOP base test case
    """

    def test_bs(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        res = BlackScholes(100, 0.10, 0.5, 1.00)
        self.assertEqual(round(res, 2), 23.93)


if __name__ == '__main__':
    unittest.main()
