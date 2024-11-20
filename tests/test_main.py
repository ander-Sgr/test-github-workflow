import unittest
from main import add, sub, mult, div

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(5, -3), 2)
        self.assertEqual(add(-5, -3), -8)
    
    def test_sub(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(-5, 3), -8)
        self.assertEqual(sub(5, -3), 8)
        self.assertEqual(sub(-5, -3), -2)

    def test_mult(self):
        self.assertEqual(mult(5, 3), 15)
        self.assertEqual(mult(-5, 3), -15)
        self.assertEqual(mult(5, -3), -15)
        self.assertEqual(mult(-5, -3), 15)

    def test_div(self):
        self.assertEqual(div(5, 3), 5/3)
        self.assertEqual(div(-5, 3), -5/3)
        self.assertEqual(div(5, -3), -5/3)
        self.assertEqual(div(-5, -3), 5/3)
        self.assertEqual(div(5, 0), "Can't posible divide to zero")