def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for elem in range(1, n):
            next_value = fib_sequence[elem] + fib_sequence[elem - 1]
            fib_sequence.append(next_value)
        return fib_sequence


def fibonacci_course_version(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        fib_sequence.extend(map(lambda i: fib_sequence[i - 1] + fib_sequence[i - 2], range(2, n)))
        return fib_sequence


if __name__ == '__main__':
    print(fibonacci(10))
