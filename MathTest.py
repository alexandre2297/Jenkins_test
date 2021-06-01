import unittest

from Math import Math

class MathTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Math.add(1,1), 2)