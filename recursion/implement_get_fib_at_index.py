'''
    given a an index, return its fib number

    Fib nums and index:
        NUMBER 0   1   1   2   3   5   8   13  21  34  55  89  144
        INDEX  0   1   2   3   4   5   6   7   8   9   10  11  12
'''


def find_fib_at_index_iterative(index):
    '''
        generate all fib(0 .. n inclusive)
        fibs generated in order of :
            - fib(0)
            - fib(1)
            - fib(2)
        return (index, fib number) at given index
    '''
    if index == 0 or index == 1:
        return (index, index)

    # starting with index 2:
    #   fib_cur = fib_prev + fib_prev_prev
    #           = prev_1 + prev_2
    prev_1 = 1
    prev_2 = 0
    for i in range(2, index+1):
        val = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = val
        if i == index:
            return i, val


def find_fib_at_index_iterative_2(index):
    '''
        build an internal array to hold all intermediate fib nums, from index 0 .. (n-1)
        fib(0) = 0
        fib(1) = 1
        fib(2) = fib(1) + fib(0)

        return (index, fib number) at given index
    '''
    internal_fibs = [0, 1]

    if index == 0 or index == 1:
        return (index, index)

    for i in range(2, index+1):
        internal_fibs.append(internal_fibs[i - 2] + internal_fibs[i - 1])

    return index, internal_fibs[index]


def find_fib_at_index_recursive(index):
    '''
        return (index, fib number) at given index
        fibs generated in order of:
             - fib(index)
             - fib(index - 1)
    '''
    if index == 0:
        return 0, 0

    if index == 1:
        return 1, 1

    prev_1_index, prev_1 = find_fib_at_index_recursive(index - 1)
    prev_2_index, prev_2 = find_fib_at_index_recursive(index - 2)
    return index, prev_1 + prev_2


if __name__ == "__main__":

    max_index = 14

    print(f'FIND FIBONACCI NUMBER AT INDEX i ITERATIVELY .....')
    # function returns (index, val)
    fib_nums = [find_fib_at_index_iterative(x) for x in range(max_index)]
    print(f'{fib_nums}')

    print(f'FIND FIBONACCI NUMBER AT INDEX i ITERATIVELY (version 2).....')
    # function returns (index, val)
    fib_nums = [find_fib_at_index_iterative_2(x) for x in range(max_index)]
    print(f'{fib_nums}')

    print(f'FIND FIBONACCI NUMBER AT INDEX i RECURSIVELY .....')
    # function returns (index, val)
    fib_nums = [find_fib_at_index_recursive(x) for x in range(max_index)]
    print(f'{fib_nums}')
