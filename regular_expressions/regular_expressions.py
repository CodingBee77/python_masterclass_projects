import re

# String value contains value from the pattern
string = "bca"
pattern = "b"

if re.search(pattern, string):
    print("Match found")
else:
    print("No match found")

# Find a pattern with 0 or more letter b in a string
# string = "bc"
# pattern = "ab*c"

# + means that the character preceeding it must be present at least 1 time
string = "aaaaabc"
pattern = "a+bc"

# Curly braces {} -> repeat a particular character exactly x times
# string = "abbc" # Matching string
# string = "ab" # Not-matching string
# pattern = "ab{2}c"

# repeat a particular character minimally x times
# string = "abbc" # Matching string
# string = "abc" # Not-matching string
# pattern = "ab{2,}c"
#
# if re.match(pattern, string):
#     print("Match found")
# else:
#     print("No match found")
