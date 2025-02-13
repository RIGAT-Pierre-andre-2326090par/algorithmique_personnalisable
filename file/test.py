import unittest

from compile import *


class MyTestCase(unittest.TestCase):
    def test_split_by_space(self):
        self.assertEqual(split_by_space('Hello World!'),
                         ['Hello', 'World!'])

    def test_split_by_line(self):
        self.assertEqual(split_by_line('Hello\nWorld!'),
                         ['Hello\n', 'World!'])

    def test_split_program(self):
        self.assertEqual(split_program('Afficher "Hello World!".'),
                         [['Afficher', '"Hello World!"', '.']])


if __name__ == '__main__':
    unittest.main()
