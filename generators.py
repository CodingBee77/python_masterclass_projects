from collections.abc import Iterator


def function():
    counter = 0
    while counter <= 10:
        yield counter
        counter += 1


def even_generator(x: int) -> Iterator[int]:
    for i in range(x):
        if i % 2 == 0:
            yield i


if __name__ == '__main__':
    print(function())  # This creates a generator object
    print(list(even_generator(10)))