from postcode_formatter import PostcodeFormatter

def get_user_input():
    """
    Get user input for postcode.
    """
    postcode = input("Please enter a postcode: ")
    return postcode

def main():
    print("Welcome to the UK postcode formatter.")
    while True:
        postcode = get_user_input()
        cleaned_postcode = PostcodeFormatter.clean_and_validate_postcode(postcode)
        if cleaned_postcode:
            print(f"Valid postcode: {cleaned_postcode}")
        else:
            print("Invalid postcode")

        new_test = input("Do you want to test another postcode? (y/n): ")

        if new_test.lower() == "n":
            print("Closing program.")
            break


main()