# Scurri-Puzzle
Scurri dev role application take home project

Puzzle sections:

1. Tell us about one thing you are proud of in your career. It could be a difficult technical problem you had to solve in your work or a personal project. There is no need to go into details; a short paragraph explaining the problem and why you are proud of it would be fine. <sub>[Jump to Section](#section-1)</sub>


2. Write a program that prints the numbers from 1 to 100. But for multiples of three print “Three” instead of the number and for the multiples of five print “Five”. For numbers which are multiples of both three and five print “ThreeFive”. <sub>[Jump to Section](#section-2)</sub>


3. Write a library that supports validating and formatting post codes for UK. The details of which post codes are valid and which are the parts they consist of can be found at [Postcodes_in_the_United_Kingdom](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting). The API that this library provides is your choice. <sub>[Jump to Section](#section-3)</sub>


## Section 1 <a id=section-1></a>

A project that I am particularly proud of is [my final project](https://github.com/ItsAlanK/apr-breathwork) from my Full-Stack Development course with Code Institute. I am very happy with the results both in the development and documentation. It was a large project that required a lot of time and effort to get right. I also found it very valuable as it gave me the opportunity to learn about relational databases, Django and a bit of AWS and API's while also getting more comfortable with more complex projects and Python in general. I enjoy the process or setting up, structuring and documenting projects so I spent a lot of time getting things right there and I feel that it shows in the README and file structure.

## Section 2 <a id=section-2></a>

See [print_numbers.py](./print_numbers/print_numbers.py)

- Program prints numbers by looping through range of values 1-100.
- Before printing number, checks for if each numbers is a multiple of 3 & 5 while iterating to print "ThreeFive". Else ->
- Checks if number is a multple of 3 to print "Three" (More common than mults of 5 so check this first). Else ->
- Checks if number is a multiple of 5 to print "Five"
- Prints iteration number if no multiples are found.

## Section 3 <a id=section-3></a>

See [postcode_formatter.py](./postcode_formatter/postcode_formatter.py)

### Rules for Postcode formatting (UK)
- Postcodes broken up into Outward and Inward code
- Alphanumeric with 6 - 8 characters (including a space)
- Outward Code:
    - Before single space
    - 2-4 Characters long
    - Starts with 1-2 letters
    - Ends with 1 digit, 2 digits or 1 digit + 1 letter
- Inward Code:
    - 3 characters long
    - 1 digit, followed by...
    - 2 characters (alphabetic)

Regular Expression provided by Wikipedia including special cases like oversea territories to be used for validation: `^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$`

### Postcode Formatter lib
Postcode Formatter library provides a class `PostcodeFormatter` which contains methods for validating a given postcode, formatting a given postcode and doing both at once.

- `PostcodeFormatter.is_valid` takes a postcode as an argument and checks against the UK postcodes format regular expression mentioned above to validate a postcode without processing or changing it. *Spaces are not taken into consideration but it is case sensitive*
- `PostcodeFormatter.format_postcode` takes a postcode as an argument, then:
    - strips away any special characters
    - removes spaces
    - sets all characters to upper case
    - adds a space before the last 3 characters

    This method does require that the correct amount of characters are provided as it would not know which ones to strip away if excess characters are present. Advisable to use `is_valid` after formatting to confirm if it is now a valid postcode.
- `PostcodeFormatter.clean_and_validate_postcode` takes a postcode as an argument and first applies the `format_postcode` method. It then uses the `is_valid` method to decide whether to return the formatted postcode if it is valid or `None` if it is not valid. This combines the two previous methods into one to save running each if both are desired.

## Running files
- To run the Print Numbers module, from the main `Scurri-Puzzle` directory run to command: 
    ```
    python3 print_numbers/print_numbers.py
    ```
- To run the Postcode Formatter file, from the main `Scurri-Puzzle` directory run to command:
    ```
    python3 postcode_formatter/postcode_formatter.py
    ```

    - For unit tests to check formatter run
        ```
        python3 postcode_formatter/test_postcode_formatter.py
        ```