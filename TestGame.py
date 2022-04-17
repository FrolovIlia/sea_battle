import unittest
import Sandbox
import main


class TestCalc(unittest.TestCase):

    def test_add_ships(self):
        clear_field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        finish_field = [['s', 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        ['s', 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 's'],
                        ['s', 's', 's', 0, 0, 0, 0, 0, 0, 's'],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 's'],
                        [0, 0, 's', 's', 's', 's', 0, 0, 0, 's'],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 's'],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 's', 's', 's', 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(main.add_ships(clear_field), finish_field)

    def test_add(self):
        self.assertEqual(Sandbox.add(3, 6), 9)

    def test_is_positive(self):
        self.assertTrue(Sandbox.is_positive(1))


if __name__ == '__main__':
    unittest.main()
