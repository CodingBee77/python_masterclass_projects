import re

sentence = "The meeting is scheduled at 9 AM."
# Shorthand for finding numbers, equivalent to [0-9]
pattern = r"\d"
numeric_characters = re.findall(pattern, sentence)
print(numeric_characters)

# Shorthand for finding non digit characters from 0-9
pattern_non_digit = r"\D"
non_digit_characters = re.findall(pattern_non_digit, sentence)
print(non_digit_characters)