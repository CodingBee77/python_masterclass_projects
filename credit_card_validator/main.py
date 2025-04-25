card_number = "5610591081018250"


def luhn_algorithm(card_number: str):
    if len(card_number) != 16:
        print(f"{card_number} is not a valid card number")
        return
    odd_sum = sum(int(digit) for digit in card_number[1::2])
    even_numbers = [int(digit) for digit in card_number[0::2]]
    double_even_numbers = [digit * 2 for digit in even_numbers]

    double_even_numbers_one_digit = [int(str(digit)[0]) + int(str(digit)[1]) if len(str(digit)) > 1 else digit for digit
                                     in double_even_numbers]
    double_even_numbers_one_digit_sum = sum(double_even_numbers_one_digit)
    total_sum = odd_sum + double_even_numbers_one_digit_sum
    if total_sum % 10 == 0:
        print(f"{card_number} is a valid card number")
    else:
        print(f"{card_number} is not a valid card number")


luhn_algorithm(card_number)
