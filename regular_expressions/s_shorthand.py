import re

sentence = "The var is \t my_var34r2324 .,;'! \n"

# \s stands for “whitespace character”, which characters this actually includes, depends on the regex flavor.
# Here it catches whitespaces and \n and \t without the exclamation mark
# pattern = r"\s"

# S stands for string without any other characters: spaces, new lines , punctiations etc -> non white space characters
# pattern = r"\S"

# S+ -> all words with characters like .,;'
pattern = r"\S+"


matches = re.findall(pattern, sentence)
print(matches)