import unittest


class Tests(unittest.TestCase):
    def test_failure(self):
        self.assertEqual(1+1, 2)
        self.assertEqual(42, 42)
        self.assertEqual(1+2, 3)

    def test_success(self):
        self.assertEqual(1+1, 2)
