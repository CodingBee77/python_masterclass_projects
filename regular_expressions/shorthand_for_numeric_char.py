import re

sentence = "The meeting is scheduled at 9 AM."
# Shorthand for finding numbers, equivalent to [0-9]
pattern = r"\d"
digit_characters = re.findall(pattern, sentence)
print(f"Digit characters using \d : {digit_characters}.")

# Shorthand for finding non digit characters from 0-9
pattern_non_digit = r"\D"
non_digit_characters = re.findall(pattern_non_digit, sentence)
print(f"Nondigit characters using \d : {non_digit_characters}.")