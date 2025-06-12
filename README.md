## Password Checker Tool

# Overview:

The Password Checker is a Python-based security tool that evaluates the strength of user-provided passwords and checks whether they have appeared in known data breaches.

# How the Program Works:

    Criteria Definition: The program checks for five criteria:
        Length of at least 8 characters.
        At least one uppercase letter.
        At least one lowercase letter.
        At least one digit.
        At least one special character (from a defined set).

   Criteria Evaluation: It uses regular expressions to check for the presence of uppercase letters, lowercase letters, numbers, and special characters.

    Strength Assessment: The program counts how many criteria are met and assigns a strength level:
        Weak: Fewer than 3 criteria met.
        Moderate: Exactly 3 criteria met.
        Strong: More than 3 criteria met.

    User Input: The user is prompted to enter a password, and the program evaluates and prints the strength of the password.

# Example Usage:

You can run the program by executing passwordchecker.py using Python 3, and it will prompt you to enter a password. Based on the input, it will provide feedback on the strength of the password.
