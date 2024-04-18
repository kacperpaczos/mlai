# test_c45.py

import unittest
from algorithm.c45 import c45
import math

# Definiowanie klasy do testowania algorytmu c45
class TestC45(unittest.TestCase):
    # Funkcja do testowania obliczania entropii dla różnych zestawów danych
    # def test_entropy_uniform(self):
    #     c45_instance = c45()
    #     data = [1, 1, 1, 1, 1, 1]
    #     result = c45_instance.entropy(data, base=2)
    #     self.assertAlmostEqual(result, 2.584962500721156, places=5)

    # def test_entropy_balanced(self):
    #     c45_instance = c45()
    #     data = [1, 2, 1, 2, 1, 2]
    #     result = c45_instance.entropy(data, base=2)
    #     self.assertAlmostEqual(result, 2.5032583347756456, places=5)

    # def test_entropy_unbalanced(self):
    #     c45_instance = c45()
    #     data = [1, 1, 1, 1, 2, 3]
    #     result = c45_instance.entropy(data, base=2)
    #     self.assertAlmostEqual(result, 2.4193819456463714, places=5)

    # def test_entropy_all_unique(self):
    #     c45_instance = c45()
    #     data = [1, 2, 3, 4, 5, 6]
    #     result = c45_instance.entropy(data, base=2)
    #     self.assertAlmostEqual(result, 2.3983029951155594, places=5)

    # def test_entropy_empty(self):
    #     c45_instance = c45()
    #     data = []
    #     result = c45_instance.entropy(data, base=2)
    #     self.assertEqual(result, 0)

    # def test_entropy_single_value(self):
    #     c45_instance = c45()
    #     data = [1]
    #     result = c45_instance.entropy(data, base=2)
    #     self.assertEqual(result, 0)

    # def test_entropy_two_values(self):
    #     c45_instance = c45()
    #     data = [1, 2]
    #     result = c45_instance.entropy(data, base=2)
    #     self.assertAlmostEqual(result, 0.9182958340544894, places=5)

    # def test_entropy_with_zeros(self):
    #     c45_instance = c45()
    #     data = [0, 0, 0, 1, 1, 1]
    #     result = c45_instance.entropy(data, base=2)
    #     self.assertAlmostEqual(result, 1.584962500721156, places=5)

    def test_entropy_identical_distributions(self):
        c45_instance = c45()
        p = [0.25, 0.25, 0.25, 0.25]
        q = [0.25, 0.25, 0.25, 0.25]
        result = c45_instance.entropy(p, q, base=2)
        self.assertAlmostEqual(result, 0.0, places=5)

    def test_entropy_completely_different_distributions(self):
        c45_instance = c45()
        p = [1, 0, 0, 0]
        q = [0, 0, 0, 1]
        result = c45_instance.entropy(p, q, base=2)
        self.assertTrue(math.isinf(result))

    def test_entropy_distributions_with_zeros(self):
        c45_instance = c45()
        p = [0.5, 0.5, 0, 0]
        q = [0.25, 0.25, 0.25, 0.25]
        result = c45_instance.entropy(p, q, base=2)
        self.assertAlmostEqual(result, 0.6931471805599453, places=5)

    def test_entropy_distributions_with_values_close_to_zero(self):
        c45_instance = c45()
        p = [0.01, 0.01, 0.01, 0.97]
        q = [0.25, 0.25, 0.25, 0.25]
        result = c45_instance.entropy(p, q, base=2)
        self.assertAlmostEqual(result, 1.2185938242800805, places=5)

if __name__ == '__main__':
    unittest.main()



