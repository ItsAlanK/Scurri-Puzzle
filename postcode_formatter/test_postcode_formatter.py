import unittest
from postcode_formatter import PostcodeFormatter


class TestPostcodeFormatter(unittest.TestCase):
    def test_is_valid(self):
        self.assertFalse(PostcodeFormatter.is_valid("Ec1A1BB")) # Lowercase
        self.assertFalse(PostcodeFormatter.is_valid("ECCC1A1BB")) # Too many characters
        self.assertFalse(PostcodeFormatter.is_valid("EC1A1BB?")) # Special character

        self.assertTrue(PostcodeFormatter.is_valid("EC1A1BB")) # Correct format
        self.assertTrue(PostcodeFormatter.is_valid("EC1A 1BB")) # Correct format with space

    def test_format_postcode(self):
        self.assertEqual(PostcodeFormatter.format_postcode("Ec1A1BB"), "EC1A 1BB") # Lowercase
        self.assertEqual(PostcodeFormatter.format_postcode("EC 1A 1BB"), "EC1A 1BB") # Too many spaces
        self.assertEqual(PostcodeFormatter.format_postcode("Ec1A 1BB&"), "EC1A 1BB") # Special character

    def test_clean_and_validate_postcode(self):
        self.assertEqual(PostcodeFormatter.clean_and_validate_postcode("Ec1A1BB"), "EC1A 1BB") # Lowercase and missing space
        self.assertEqual(PostcodeFormatter.clean_and_validate_postcode("ECCC1A1BB"), None) # Too many characters

if __name__ == '__main__':
    unittest.main()