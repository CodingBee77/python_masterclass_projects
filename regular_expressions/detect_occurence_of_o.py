import re

# Find words with at least 1 occurences of letter o
text = "Helloooo, Python is awesomeeeee !"
# Below pattern defines word character then optional o and word character again
pattern = r"\w*o+\w*"
matches = re.findall(pattern, text)
print(matches)