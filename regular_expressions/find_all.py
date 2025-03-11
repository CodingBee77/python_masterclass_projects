import re

text = "Today the sun is shining and the birds are singing."
pattern = r"the"
matches = re.findall(pattern, text)

another_text = "The cat and the dog sat on the mat."
another_pattern = r"[abc]"
another_match = re.findall(another_pattern, another_text)
print(another_match)

sentence = "The meeting is scheduled at 9 AM."
pattern = r"[aeiouy]"
vowels = re.findall(pattern, sentence)
print(vowels)