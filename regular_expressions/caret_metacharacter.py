import re

# Caret metacharacter means that stirng needs to start with a certain string
string = "9123456765342"  # is a match
string_2 = "92834975892474932"  # not a match
pattern = r"^91"
if re.match(pattern, string):
    print("Match found")
else:
    print("No match found")
