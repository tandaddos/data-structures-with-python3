'''
    factorial(n) = n * factorial(n-1)
                 = n * (n-1) * .... * 2 * 1
                 = 1 * (2) * ... (n-1) * n

    input   = [1, 2, 3, 4, 5]
    output  = [1, 2, 6, 24, 120]
'''


def findFactorialIterative(number):
    if number == 0 or number == 1 or number < 0:
        return 1

    value = 1
    # we will use range(n), which will gives sequence upto (n-1) only
    # so have to add 1 to input
    for i in range(1, number + 1):
        value *= i
    return value


def findFactorialRecursive(number):
    if number == 0 or number == 1 or number < 0:
        return 1
    return number * findFactorialRecursive(number - 1)


def findFactorialGenerator(number):
    '''
        Use generator to compute factorial
    '''
    for i in range(number + 1):
        # if number == 0 or number == 1 or number < 0:
        #     return 1
        # value = 1
        yield findFactorialRecursive(i)


if __name__ == "__main__":
    maxnumber = 101
    numbers = [_ for _ in range(maxnumber)]

    vals = [_ for _ in findFactorialGenerator(maxnumber)]
    print(f'RECURSE VIA GENERATOR RECURSIVELY .....')
    print(vals)

    vals = [findFactorialIterative(n) for n in numbers]
    print(f'RECURSE ITERATIVELY .....')
    print(vals)

    vals = [findFactorialRecursive(n) for n in numbers]
    print(f'RECURSE RECURSIVELY .....')
    print(vals)
