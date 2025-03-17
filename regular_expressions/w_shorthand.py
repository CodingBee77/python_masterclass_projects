import re

sentence = "The var is my_var34r2324 ! \n"
#  \w stands for “word character”. It always matches the ASCII characters [A-Za-z0-9_]
# pattern = r"\w"

# \s stands for “whitespace character”, which characters this actually includes, depends on the regex flavor.
# Here it catches whitespaces and \n without the exclamation mark
# pattern = r"\s"

# W stands for whitespaces, it catches all whitespaces, exclamation mark and '\n'
pattern = r"\W"


matches = re.findall(pattern, sentence)
print(matches)