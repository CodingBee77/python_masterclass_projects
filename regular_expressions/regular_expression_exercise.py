import re

# Write a Python program to check that a string contains only a certain
# set of characters (in this case a-z, A-Z and 0-9).


def check_if_small_letters(input_value: str) -> bool:
    pattern = re.compile("[a-z]+")
    if pattern.fullmatch(input_value) is not None:
        return True
    return False


def check_if_capital_letters(input_value: str) -> bool:
    pattern = re.compile("[A-Z]+")
    if pattern.fullmatch(input_value) is not None:
        return True
    return False


def has_a_followed_by_zero_or_more_bs(input_value:str) -> bool:
    pattern = "a(b*)$"
    if re.match(pattern, input_value):
        return True
    return False


if __name__ == '__main__':
    small_letters = "asdfdghxs"
    not_small_letters = "asdfsaFDFDA"
    capital_letters = "SDHSIOHSDODS"
    not_capital_letters = "asdsHSHDUIJSDIO"
    zero_bs = "ac"
    zero_bs_2 = "abc"
    zero_bs_3 = "a"
    zero_bs_4 = "ab"
    zero_bs_5 = "abb"
    print("\n Check if string contains only small letters: ")
    print(check_if_small_letters(not_small_letters))
    print("\n Check if string contains only capital letters: \n")
    print(check_if_capital_letters(not_capital_letters))
    print("\n Check if string has an a followed by zero or more b's: \n")
    print(has_a_followed_by_zero_or_more_bs(zero_bs))
    print(has_a_followed_by_zero_or_more_bs(zero_bs_2))
    print(has_a_followed_by_zero_or_more_bs(zero_bs_3))
    print(has_a_followed_by_zero_or_more_bs(zero_bs_4))
    print(has_a_followed_by_zero_or_more_bs(zero_bs_5))


