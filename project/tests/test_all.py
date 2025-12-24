import unittest
from string_utils import uppercase_list
from generator_utils import even_odd_generator

class TestStringUtils(unittest.TestCase):
    def test_uppercase_list(self):
        self.assertEqual(uppercase_list("abc"), ["A", "B", "C"])

class TestGenerator(unittest.TestCase):
    def test_even_odd(self):
        gen = even_odd_generator()
        self.assertEqual(next(gen), "Парне")
        self.assertEqual(next(gen), "Непарне")
        self.assertEqual(next(gen), "Парне")

if __name__ == "__main__":
    unittest.main()