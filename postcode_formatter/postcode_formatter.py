import re


class PostcodeFormatter:
    """
    Class for validating and formatting UK postcodes.

    Methods:
        is_valid: Check if postcode provided is valid according to UK postcode rules.
        format_postcode: Format the postcode provided to UK format.
    """

    def is_valid(postcode):
        """
        Check if postcode provided is valid according to UK postcode rules.
        Rules found at: https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Validation
        Args:
            postcode: str
        Returns:
            bool: True if postcode is valid, False if not.
        """

        regex = r'^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$'
        return re.match(regex, postcode) is not None
    
    def format_postcode(postcode):
        """
        Format the postcode provided to UK format.
        Strings non-alphanumeric characters and converts to uppercase.
        Adds space before last 3 characters.
        Args:
            postcode: str
        Returns:
            str: Formatted postcode
        """

        cleaned_postcode = re.sub(r'[^a-zA-Z0-9]', '', postcode)
        cleaned_postcode = cleaned_postcode.upper()
        return cleaned_postcode[:-3] + " " + cleaned_postcode[-3:]

    def clean_and_validate_postcode(postcode):
        """
        Method to clean and validate a postcode to return valid postcode if possible.
        Uses cleaning and validating rules from format_postcode and is_valid methods.
        Args:
            postcode: str
        Returns:
            str: Formatted postcode if valid, None if not.
        """

        cleaned_postcode = PostcodeFormatter.format_postcode(postcode)
        if PostcodeFormatter.is_valid(cleaned_postcode):
            return cleaned_postcode
        else:
            return None
