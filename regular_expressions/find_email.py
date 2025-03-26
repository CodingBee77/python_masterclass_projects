import re

text = "Please contact me at martyna@example.com or send a message to jane@example.co"
pattern = r"\b[A-za-z0-9._%+-]+@[A-za-z0-9.-]+\.[A-Za-z]{2,}\b"

matches = re.findall(pattern, text)
print(matches)