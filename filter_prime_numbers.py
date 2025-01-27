def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    prime_numbers = list(filter(is_prime, numbers))
    print(prime_numbers)
