import unittest

from Math import Math

class MathTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Math.add(1,1), 2)

    def test_substract(self):
        self.assertEqual(Math.substract(3.0,0.5), 2.5)