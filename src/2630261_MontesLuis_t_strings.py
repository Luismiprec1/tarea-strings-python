# Student: Luis Angel Montes Hernandez
# Student ID: 2630261
# Group: IM3
# Assignment: String operations in Python
# File: 2630261_MontesLuis_t_strings.py

# Executive Summary
# A string is a text value, and its Python type is str.
# Strings are immutable, so string methods return a new value instead of changing the old one.
# With strings I can join text, count its length, take slices, search, and replace parts.
# Indexes help me read one character, while slices can take a part or reverse a string.
# Input checks are important for names, emails, passwords, and other user text.
# strip and lower can help normalize text before I compare it.
# This file has six problems with inputs, outputs, validations, and three test cases each.
# It also has the code that runs each problem from the console.

# Good Practices
# - Strings are immutable, so a change creates a new string.
# - Use strip() and lower() before comparing text when it makes sense.
# - Avoid magic numbers in slices and explain what each slice takes out.
# - Use string methods instead of rewriting simple text operations.
# - Check first that input is not empty, then check its format.
# - Use clear variable names and error messages that explain the problem.

from math import isfinite

MIN_NAME_WORDS = 2
MIN_PALINDROME_LENGTH = 3
MIN_PASSWORD_LENGTH = 8
LABEL_WIDTH = 30

# Problem 1: Full name formatter
# Description: This program cleans extra spaces in a full name.
# It shows the name in title case and makes initials from each word.
# Inputs:
# - full_name: one string with at least a first name and a last name.
# Outputs:
# - Formatted name and initials, or an error message.
# Validations:
# - The name cannot be empty after strip().
# - The name must have at least two words after split().
# Test cases:
# 1) Normal: "  JUAN   carlos tovar " -> Juan Carlos Tovar; J.C.T.
# 2) Border: "A B" -> A B; A.B.
# 3) Error: "   " -> Error: name cannot be empty.
def format_full_name(full_name):
    if not isinstance(full_name, str):
        return "Error: name must be text"

    clean_name = " ".join(full_name.strip().split())
    if clean_name == "":
        return "Error: name cannot be empty"

    name_parts = clean_name.split()
    if len(name_parts) < MIN_NAME_WORDS:
        return "Error: enter at least two words"

    formatted_name = clean_name.title()
    initials = "".join(part[0].upper() + "." for part in name_parts)
    return f"Formatted name: {formatted_name}\nInitials: {initials}"


# Problem 2: Simple email validator
# Description: This program checks a basic email structure.
# If the email passes the checks, it also shows the domain part.
# Inputs:
# - email_text: an email written as one string.
# Outputs:
# - Valid email: true or false; the domain is shown when valid.
# Validations:
# - The email cannot be empty after strip() and cannot contain spaces.
# - There must be exactly one @, a local part, and a domain with a dot.
# Test cases:
# 1) Normal: "student@school.edu" -> true; domain school.edu.
# 2) Border: "a@b.c" -> true; domain b.c.
# 3) Error: "student @school.edu" -> false because it has a space.
def validate_email(email_text):
    if not isinstance(email_text, str):
        return "Valid email: false\nError: email must be text"

    clean_email = email_text.strip()
    if clean_email == "":
        return "Valid email: false\nError: email cannot be empty"

    if any(character.isspace() for character in clean_email):
        return "Valid email: false\nError: email cannot contain spaces"

    if clean_email.count("@") != 1:
        return "Valid email: false\nError: email must have one @"

    at_position = clean_email.find("@")
    local_part = clean_email[:at_position]
    domain_part = clean_email[at_position + 1:]

    if local_part == "" or domain_part == "":
        return "Valid email: false\nError: email is missing a part"

    if "." not in domain_part or domain_part.startswith(".") or domain_part.endswith("."):
        return "Valid email: false\nError: domain needs a dot"

    return f"Valid email: true\nDomain: {domain_part}"


# Problem 3: Palindrome checker
# Description: This program checks if a phrase reads the same backwards.
# It ignores letter case and spaces, but keeps other punctuation.
# Inputs:
# - phrase: a string that should have at least three characters after cleaning.
# Outputs:
# - Is palindrome: true or false, plus the cleaned phrase.
# Validations:
# - The phrase cannot be empty after strip().
# - At least three characters must remain after spaces are removed.
# Test cases:
# 1) Normal: "Anita lava la tina" -> true; normalized: anitalavalatina.
# 2) Border: "Aba" -> true; normalized: aba.
# 3) Error: "a  " -> Error: phrase must have at least three characters.
def check_palindrome(phrase):
    if not isinstance(phrase, str):
        return "Error: phrase must be text"

    if phrase.strip() == "":
        return "Error: phrase cannot be empty"

    normalized_phrase = phrase.strip().lower().replace(" ", "")
    if len(normalized_phrase) < MIN_PALINDROME_LENGTH:
        return "Error: phrase must have at least three characters"

    is_palindrome = normalized_phrase == normalized_phrase[::-1]
    return f"Is palindrome: {str(is_palindrome).lower()}\nNormalized phrase: {normalized_phrase}"


# Problem 4: Sentence word stats
# Description: This program removes extra spaces and separates a sentence into words.
# It shows the count, first and last word, and shortest and longest word.
# Inputs:
# - sentence: one sentence as a string.
# Outputs:
# - Word count, first word, last word, shortest word, and longest word.
# Validations:
# - The sentence cannot be empty after strip().
# - At least one word must remain after split().
# Test cases:
# 1) Normal: "  Python   is great today  " -> 4 words; first Python; last today; shortest is; longest Python.
# 2) Border: "Code" -> 1 word; Code is first, last, shortest, and longest.
# 3) Error: "   " -> Error: sentence cannot be empty.
def sentence_word_stats(sentence):
    if not isinstance(sentence, str):
        return "Error: sentence must be text"

    clean_sentence = " ".join(sentence.strip().split())
    if clean_sentence == "":
        return "Error: sentence cannot be empty"

    words = clean_sentence.split()
    if len(words) == 0:
        return "Error: sentence must have a word"

    shortest_word = words[0]
    longest_word = words[0]
    for word in words[1:]:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word

    return (
        f"Word count: {len(words)}\n"
        f"First word: {words[0]}\n"
        f"Last word: {words[-1]}\n"
        f"Shortest word: {shortest_word}\n"
        f"Longest word: {longest_word}"
    )


# Problem 5: Password strength classifier
# Description: This program gives a basic strength level to a password.
# It looks at length and checks uppercase, lowercase, digits, and symbols.
# Inputs:
# - password_input: a string entered by the user.
# Outputs:
# - Password strength: weak, medium, or strong.
# Validations:
# - The password cannot be blank after strip().
# - Weak: under 8 characters, a common password, or only one character group.
# - Medium: at least 8 characters with two or three character groups.
# - Strong: at least 8 characters with upper, lower, digit, and symbol.
# Test cases:
# 1) Normal: "Violet789" -> medium because it has upper, lower, and digits.
# 2) Border: "abcdefgh" -> weak because it only has lowercase letters.
# 3) Error: "   " -> Error: password cannot be empty.
# Extra rule example: "BlueSky9!" -> strong.
COMMON_PASSWORDS = ("password", "12345678", "qwerty123")

def classify_password(password_input):
    if not isinstance(password_input, str):
        return "Error: password must be text"

    if password_input.strip() == "":
        return "Error: password cannot be empty"

    has_upper = any(character.isupper() for character in password_input)
    has_lower = any(character.islower() for character in password_input)
    has_digit = any(character.isdigit() for character in password_input)
    has_symbol = any(not character.isalnum() and not character.isspace() for character in password_input)
    group_count = sum((has_upper, has_lower, has_digit, has_symbol))
    password_length = len(password_input)
    is_common = password_input.lower() in COMMON_PASSWORDS

    if password_length < MIN_PASSWORD_LENGTH or is_common or group_count < 2:
        strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    else:
        strength = "medium"

    return f"Password strength: {strength}"


# Problem 6: Product label formatter
# Description: This program makes a product label with a fixed width of 30 characters.
# Short labels get spaces at the end and long labels are cut to fit.
# Inputs:
# - product_name: a non-empty product name.
# - price_value: a positive number or text that can be converted to a number.
# Outputs:
# - A quoted label and its length, which must be 30.
# Validations:
# - The product name cannot be empty after strip().
# - Price must convert to a finite number greater than zero.
# Test cases:
# 1) Normal: "Book", "12.5" -> "Product: Book | Price: $12.5  "; length 30.
# 2) Border: "A", "0.01" -> label is padded to length 30.
# 3) Error: "Pen", "0" -> Error: price must be positive.
def format_product_label(product_name, price_value):
    if not isinstance(product_name, str):
        return "Error: product name must be text"

    clean_product = " ".join(product_name.strip().split())
    if clean_product == "":
        return "Error: product name cannot be empty"

    try:
        if isinstance(price_value, str):
            numeric_price = float(price_value.strip())
        else:
            numeric_price = float(price_value)
    except (ValueError, TypeError, OverflowError):
        return "Error: price must be a number"

    if not isfinite(numeric_price):
        return "Error: price must be finite"
    if numeric_price <= 0:
        return "Error: price must be positive"

    price_text = format(numeric_price, "g")
    base_label = f"Product: {clean_product} | Price: ${price_text}"

    if len(base_label) > LABEL_WIDTH:
        label_text = base_label[:LABEL_WIDTH]
    else:
        label_text = base_label + " " * (LABEL_WIDTH - len(base_label))

    return f"Label: '{label_text}'\nLength: {len(label_text)}"


# Main program: enter one value for each problem.
def main():
    print("STRING PRACTICE")
    print("Enter one value for each problem.")

    full_name = input("Problem 1 - full name: ")
    print(format_full_name(full_name))
    print()

    email_text = input("Problem 2 - email: ")
    print(validate_email(email_text))
    print()

    phrase = input("Problem 3 - phrase: ")
    print(check_palindrome(phrase))
    print()

    sentence = input("Problem 4 - sentence: ")
    print(sentence_word_stats(sentence))
    print()

    password_input = input("Problem 5 - password: ")
    print(classify_password(password_input))
    print()

    product_name = input("Problem 6 - product name: ")
    price_value = input("Problem 6 - price: ")
    print(format_product_label(product_name, price_value))


if __name__ == "__main__":
    main()

# Conclusions
# I learned that string methods make text tasks shorter and easier to read.
# strip and split help when a user adds extra spaces.
# lower is good before comparing text that can have different letter case.
# Clear checks keep empty or wrong information from being used in the program.
# A string does not change in place; methods and slices make new results.
# Slices helped me take parts of the email and limit a label to 30 characters.
# Becuase inputs are not always clean, validation is useful in a program.

# References
# 1) Python documentation - Text Sequence Type: str
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python documentation - String Methods
#    https://docs.python.org/3/library/stdtypes.html#string-methods
# 3) Python documentation - Built-in Functions (input, float, len)
#    https://docs.python.org/3/library/functions.html
# 4) Python Tutorial - Input and Output (formatted strings)
#    https://docs.python.org/3/tutorial/inputoutput.html
# 5) Python Tutorial - Data Structures
#    https://docs.python.org/3/tutorial/datastructures.html
