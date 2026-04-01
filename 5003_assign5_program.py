"""
CY 5003 Spring 2026
Katie Goldenberg
February 5, 2026

This program checks whether a course code input by
the user is included in Northeastern's MS in Cybersecurity 
Align Course Bridge and Core Requirements
catalogue. The program validates whether the input
is the correct range, length, and "pattern." It then checks
whether the code is in the catalogue. If the code is in the
catalogue, it indicates whether the course is a Bridge course
or Core Requirement.
"""

import re # imports "re" to use for pattern matching

def validate_range(input):
    """
    Checks whether the numeric section of the input course 
    code is in the correct numeric range string.
    If not in the correct range, raises a ValueError.
    If in the correct range, returns the input.
    """

    parts = input.split() # breaks string into letters + nums
    if not (5000 <= int(parts[1]) <= 8000): # checks range of code num
        raise ValueError("Code number not in correct range.")
        # raises ValueError if num is not between 5000 and 8000
    return input # if input is in the right range, returns input

def validate_length(input):
    """
    Checks whether the input course code is the correct
    course code length (7 characters). If the input is
    not 7 chars, raises a  ValueError. If the input is
    the correct length, returns the input.
    """

    if len(input) != 7: # checks the length of the input
        raise ValueError("Course code must be 7 characters.")
        # raises error if input is not 7 chars
    return input # if input is 7 chars, returns input

def validate_pattern(input):
    """Checks whether the input course code is in the
    correct format (two letters, one space, and four digits).
    If the input is not in the correct format, raises
    a ValueError. If the input is the correct length, 
    returns the input."""

    pattern = r'^[A-Z]{2}\s\d{4}$' # defines course code format
    if not re.match(pattern, input):
        raise ValueError("Invalid course code format.")
        # raises error if the input does not match the format
    return input # if it matches the format, returns input

def validate_input(input):
    """Runs user input through each validation function.
    Returns input."""

    user_input = validate_range(input) # checks type
    user_input = validate_length(input) # checks length
    user_input = validate_pattern(input) # checks pattern
    return user_input # returns input

def main():
    """Main function. Prompts user for course code input.
    Runs the input through input validation function.
    If input does not raise errors, checks if course is in
    lists of Bridge courses or Core Requirements. If not
    in either list, prints "course not found" statement.
    Also prints required output statement."""

    bridge_lst = ["CS 5001", "CS 5003", "CS 5002", "CY 5001",
                  "CY 5003"] # list of bridge courses
    
    core_lst = ["CY 5010", "CY 5120", "CY 5130", "CY 5150",
                "CY 5770", "CY 6120", "CY 6740", "CY 6760",
                "CY 5200", "CY 5210", "CY 5240", "CY 5250",
                "CY 6200", "CY 7900"] # list of core courses
    
    try: # try block
        course = input("Please enter a course code." + 
                   " Please use the format 'CY 0000': ") 
        # prompts user for input

        validated = validate_input(course) # stores as variable
        # if input does not raise ValueError
        if course in bridge_lst: # checks if in "Bridge" list
            print("You have entered a Bridge course.")
        elif course in core_lst: # checks if in "Core" list
            print("You have entered a Core Requirement.")
        else: # if input is not in either list
            print("This is not in Northeastern's MSCY Align catalogue.")
        
        print("This Python program performs three types of input " \
                "validation (type, length, and pattern matching) " \
                "on the course code and uses the Pylint static " \
                "analyzer. Programmed by Katie Goldenberg on February " \
                "5, 2026.") # required print statement

    except ValueError as e: # exception if ValuError occurs
        print("Validation error:", e) # prints error statement

        print("This Python program performs three types of input " \
                "validation (range, length, and pattern matching) " \
                "on the course code and uses the Pylint static " \
                "analyzer. Programmed by Katie Goldenberg on February " \
                "5, 2026.") # required print statement

if __name__ == "__main__":
    main() # runs main function


    
