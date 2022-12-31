from main import Factorial
import unittest


class TestMyFactoral(unittest.TestCase):
    def test_negative_number(self):
        res = Factorial(-1)
        self.assertEqual(res, None)

    def test_positive_small_number(self):
        res = Factorial(5)
        self.assertEqual(res, 120)

    def test_incorrect_input(self):
        res = Factorial("hahaha")
        self.assertEqual(res, None)


suite = unittest.TestLoader().loadTestsFromTestCase(TestMyFactoral)
unittest.TextTestRunner(verbosity=2).run(suite)
