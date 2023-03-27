import unittest
from string_functions import *

class TestToUpper(unittest.TestCase):
    def test_all_lowercase_string(self):
        self.assertEqual('BALTAZAR', to_upper('baltazar'))

    def test_string_with_other_characters(self):
        self.assertEqual('BA*TA_AR', to_upper('bA*Ta_aR'))
        self.assertEqual('123BALTAZAR56', to_upper('123baltazar56'))
        self.assertEqual('123BALT$%^AZAR4+', to_upper('123BalT$%^AzaR4+'))

    def test_empty_string(self):
        self.assertEqual('', to_upper(''))

    def test_all_uppercase_string(self):
        self.assertEqual('BALTAZAR', to_upper('BALTAZAR'))


class TestToLower(unittest.TestCase):
    def test_all_uppercase_string(self):
        self.assertEqual('baltazar', to_lower('BALTAZAR'))
    
    def test_string_with_other_characters(self):
        self.assertEqual('ba*ta_ar', to_lower('bA*Ta_aR'))
        self.assertEqual('123baltazar56', to_lower('123baltazar56'))
        self.assertEqual('123balt$%^azar4+', to_lower('123BalT$%^AzaR4+'))
    
    def test_empty_string(self):
        self.assertEqual('', to_upper(''))
    
    def test_all_lowercase_string(self):
        self.assertEqual('baltazar', to_lower('baltazar'))


class TestCapitalize(unittest.TestCase):
    def test_qll_lowercase_string(self):
        self.assertEqual('Baltazar', capitalize('baltazar'))
    
    def test_strings_with_other_characters(self):
        self.assertEqual('Ba*ta_ar', capitalize('bA*Ta_aR'))
        self.assertEqual('B123altazar56', capitalize('b123altazar56'))
        self.assertEqual('123balt$%^azar4+', capitalize('123BalT$%^AzaR4+'))
    
    def test_empty_string(self):
        self.assertEqual('', capitalize(''))
    
    def test_capitalized_string(self):
        self.assertEqual('Baltazar', capitalize('Baltazar'))

if __name__ == '__main__':
    unittest.main()
