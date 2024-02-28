import re

# TEST REGEX
# text = "Hello"
# x = re.match("^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$", text)

# if(x):
#     print("Valid postcode")
# else:
#     print("Invalid postcode")

class PostcodeFormatter:
    
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
        Args:
            postcode: str
        Returns:
            str: Formatted postcode
        """
        postcode = postcode.upper()
        postcode = postcode.replace(" ", "")
        return postcode[:-3] + " " + postcode[-3:]

# TEST IS VALID METHOD
pc = "Ec1A1BB"
print(PostcodeFormatter.is_valid(pc)) 
print(PostcodeFormatter.format_postcode(pc))
print(PostcodeFormatter.is_valid(PostcodeFormatter.format_postcode(pc))) 