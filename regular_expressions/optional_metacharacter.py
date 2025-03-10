# the character preceding ? is optional - it may or not be present
import re

string = "pythonfile" # will work as well
pattern = r"python-?file"
if re.match(pattern,string):
    print("Match found")
else:
    print("No match found")