def square(x: int):
    return x ** 2


if __name__ == '__main__':
    # Lambda function with 3 arguments
    result = (lambda x,y,z: x+y/z)(4,5,6)
    print(result)

    # Default parameters:
    result = (lambda x=10,y=2,z=45: x+y/z)(4)
    print(result)

    # Maps
    numbers = [4, 6, 7, 3, 2, 34]

    # Calculate square of number using map function
    new_list = list(map(square, numbers))
    print(new_list)

    # Calculate 5% discount for all prices
    prices = [100, 200,300, 400, 500]
    prices_with_discount = list(map(lambda x: x - x*0.05, prices))
    print(prices_with_discount)

    names = ['john']