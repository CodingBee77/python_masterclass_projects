import re

# Write a pattern that matches both python and Python and Cython
string = "Cython"
pattern = r"[CPp]ython"
if re.match(pattern, string):
    print("Match found")
else:
    print("No match found")
#############################
# String matches the pattern when small letters from a-z are used, similarly with A-Z
string_2 = "abcd"
patter_2 = r"[a-z]"
if re.match(pattern, string):
    print("Match found")
else:
    print("No match found")
