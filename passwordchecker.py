import re


def evaluate_password_strength(password):

    # Initialize strength criteria

    length_criteria = len(password) >= 8

    uppercase_criteria = re.search(r'[A-Z]', password) is not None

    lowercase_criteria = re.search(r'[a-z]', password) is not None

    number_criteria = re.search(r'[0-9]', password) is not None

    special_char_criteria = re.search(r'[@$!%*?&]', password) is not None


    # Count the number of criteria met

    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])


    # Determine password strength

    if criteria_met < 3:

        return "Weak"

    elif criteria_met == 3:

        return "Moderate"

    else:

        return "Strong"


# Get user input

password = input("Enter a password to evaluate its strength: ")

strength = evaluate_password_strength(password)

print(f"Password strength: {strength}")
