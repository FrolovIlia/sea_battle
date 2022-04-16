import unittest
import Sandbox



class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Sandbox.add(3, 6), 9)

    def test_is_positive(self):
        self.assertTrue(Sandbox.is_positive(1))

if __name__ == '__main__':
    unittest.main()
