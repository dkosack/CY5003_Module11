"""
Name: Daria Kosack
Date: February 18, 2026
Program: cy5003_module_7_password_checker.py
Description:
    This Python program checks whether a password is weak or strong.
    It asks for personal information and a password in a loop until the user types 'e' to exit.
    It checks whether the password contains personal information 
    and whether it follows strong password guidance.
    
    Password strength techniques referenced:
    1) CISA "Use Strong Passwords" guidance: 
        make passwords long (16+), random, and unique (CISA, n.d.)
    2) NIST "How Do I Create a Strong Password?" guidance: 
        make passwords long (15+), avoid common/compromised passwords (NIST, 2025) 
"""

import time

# Allowed characters (whitelist)
ALLOWED = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
    "!@#$%^&*_-"
)
# Security Issue: The password whitelist is limited to letters, numbers, and a few symbols. 
# This could lead to users creating passwords that are less secure because they are limited in character variety. 
# To fix this, we could expand the whitelist to include a wider range of symbols and special characters, 
# which would encourage users to create more complex and secure passwords.

# Common weak passwords
COMMON = {
    "password", "password1", "password!", "12345678", "password123",
    "123", "123456", "admin", "123456789", "p@ssw0rd"
}

def clean_text(text):
    """ Make text safe to compare: strip spaces and lowercase. """
    # Type checking validation (#1)
    if not isinstance(text, str):
        raise ValueError("Input must be text.")
    # Return cleaned text
    return text.strip().lower()


def validate_birth_year(year_text):
    """ Validate birth year with range checking. """
    # Type checking (#1)
    if not isinstance(year_text, str):
        raise ValueError("Birth year must be text.")
    year_text = year_text.strip()
    if not year_text.isdigit() or len(year_text) != 4:
        raise ValueError("Birth year must be 4 digits (YYYY).")
    year = int(year_text)
    # Range checking (#2)
    if year < 1900 or year > 2026:
        raise ValueError("Birth year must be between 1900 and 2026.")
    return year_text


def validate_password(pw):
    """ Validate password with type checking, length validation, and whitelist. """
    # Type checking (#1)
    if not isinstance(pw, str):
        raise ValueError("Password must be text.")
    pw = pw.strip()
    if pw == "":
        raise ValueError("Password cannot be empty.")
    # Length validation (#3)
    if len(pw) < 15:
        raise ValueError("Password must be at least 15 characters long.")
    # Whitelist (#4)
    for ch in pw:
        if ch not in ALLOWED:
            raise ValueError(
                "Password contains invalid characters. "
                "Letters, numbers, and these symbols (!@#$%^&*_-) only."
                )
    return pw


def contains_personal_info(password, first, last, birth_year):
    """ 
    Check password against personal information. 
    1) First name
    2) Last name
    3) Birth year
    """
    pw_norm = clean_text(password)
    first_token = clean_text(first)
    last_token = clean_text(last)
    year_token = clean_text(birth_year)
    # If password contains any personal token, return True
    if first_token in pw_norm:
        return True
    if last_token in pw_norm:
        return True
    if year_token in pw_norm:
        return True
    return False


def variety_score(password):
    """ 
    Simple counter:
        +1 lower
        +1 upper
        +1 digit
        +1 symbol
    """
    lower = 0
    upper = 0
    digit = 0
    symbol = 0
    for ch in password:
        if ch.islower():
            lower = 1
        elif ch.isupper():
            upper = 1
        elif ch.isdigit():
            digit = 1
        elif ch in "!@#$%^&*_-":
            symbol = 1
    return lower + upper + digit + symbol


def contains_common_patterns(password):
    """ Check for extremely common patterns. """
    pw_norm = clean_text(password)
    if "password" in pw_norm or "admin" in pw_norm or "qwerty" in pw_norm:
        return True
    if "123" in pw_norm or "123456" in pw_norm or "12345678" in pw_norm:
        return True
    return False


def assess_password(password, first, last, birth_year):
    """ Return weak/strong and reasons, with CISA/NIST notes. """
    reasons = []
    pw_norm = clean_text(password)
    # NIST: Avoid common/guessable passwords
    if pw_norm in COMMON:
        reasons.append("Common password (NIST).")
    # NIST: Detect common patterns
    if contains_common_patterns(password):
        reasons.append("Contains commonly used pattern.")
    # CISA + NIST: Avoid personal info
    if contains_personal_info(password, first, last, birth_year):
        reasons.append("Contains personal info (CISA + NIST).")
    # NIST: Length 15+ characters
    if len(password) < 15:
        reasons.append("Shorter than 15 characters (NIST).")
    # CISA: Length 16+ characters
    if len(password) < 16:
        reasons.append("Shorter than 16 characters (CISA).")
    # CISA: "Random guidance" (have variety)
    if variety_score(password) < 3:
        reasons.append("Low character variety (CISA).")
    # Automatically weak if common or contains personal info
    if pw_norm in COMMON or contains_common_patterns(password) or contains_personal_info(password, first, last, birth_year):
        label = "Weak"
    # Strong if not containing multiple weaknesses
    elif len(reasons) >= 2:
        label = "Weak"
    else:
        label = "Strong"
    return label, reasons
# Security Issue: There is no limit to how many times the user can attempt to enter a password, 
# which could lead to an infinite loop if the user keeps entering invalid passwords. Makes this open to brute-force attacks. 
# To fix this, we could implement a counter to limit the number of attempts and exit the loop after a certain number of failed attempts.

def main():
    """ Main loop: runs until user types 'e'. """
    print(
        "This Python program checks the strength of a password. \n"
        "Program name: cy5003_module_7_password_checker.py. \n"
        "Programmed by Daria Kosack on February 18, 2026."
    )
    print()
    time.sleep(1)
    while True:
        try:
            first = input("Enter your first name: ")     
            last = input("Enter your last name: ")
            birth_year = validate_birth_year(input("Enter your birth year (YYYY): "))
            pw_input = input("Enter a password to check (or type 'e' to exit): ")
            if pw_input.strip().lower() == "e":
                print("\nExiting program. Goodbye.")
                break
            pw = validate_password(pw_input)
            label, reasons = assess_password(pw, first, last, birth_year)
            print(f"\nPassword result: {label}")
            if reasons:
                print("Rationale:")
                for r in reasons:
                    print(f"- {r}")
            else:
                print("Rationale:")
                print("- No weaknesses detected based on NIST and CISA guidance.")
        except ValueError as e:
            print(f"\nInput error: {e}")
            print("Please try again.")
# Security Issue: There is no validation on first and last name inputs. If the user presses enter without typing anything, 
# the program will consider an empty string as a valid name. 
# This could lead to false positives when checking for personal information in the password, 
# as an empty string is technically contained in any password. 
# To fix this, we should add validation to ensure that the first and last name inputs are not empty and do not contain only whitespace.

if __name__ == "__main__":
    main()
