numbers = [1,2,3,4,5,6,7,8,9,10]

def odd(x):
    if x%2 ==1:
        return x


if __name__ == '__main__':
    odd_numbers = list(filter(odd, numbers))
    # OR
    odd_numbers_with_lambda = list(filter(lambda x: x%2==1, numbers))

    print(odd_numbers)
    print(odd_numbers_with_lambda)