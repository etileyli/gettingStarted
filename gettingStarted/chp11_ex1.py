import unittest
from names_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py"""

    def test_first_last_name(self):
        """Do names like 'Emre Tileylioglu work?"""
        formatted_name = get_formatted_name('emre', 'tileylioglu')
        self.assertEqual(formatted_name, 'Emre Tileylioglu')

    def test_first_middle_last_name(self):
        """Do names like 'Emre Ebru Tileylioglu work?"""
        # formatted_name = get_formatted_name(first='emre', middle='ebru', last='tileylioglu')
        formatted_name = get_formatted_name(first='emre', middle='ebru', last='tileylioglu')
        self.assertEqual(formatted_name, 'Emre Ebru Tileylioglu')


unittest.main()
