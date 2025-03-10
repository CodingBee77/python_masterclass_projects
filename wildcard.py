# . symbol can take place of any other symbol
# Example: "a.b" - we can place any character between a and b

import re

# string = "acab" # wont match because between a and b we have 2 characters
string = "acbb" # will match because acb match the pattern and last b is after the pattern
pattern = r"a.b"
if re.match(pattern,string):
    print("Match found")
else:
    print("No match found")