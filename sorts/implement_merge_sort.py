'''
    Implement merge sort recursively

    return an new sorted array
'''


def sort_merge_recursive(arr):
    if len(arr) == 1:
        # return the whole array instead of only the single element
        # this is because the merging routine takes arrays as inputs
        return arr

    # split input in two parts
    half_len = int(len(arr) / 2)
    left = arr[:half_len]
    right = arr[half_len:]

    # print(f' left  = {left}')
    # print(f' right = {right}')

    # sort each part
    left_sorted = sort_merge_recursive(left)
    right_sorted = sort_merge_recursive(right)

    # print(f' left_sorted  = {left_sorted}')
    # print(f' right_sorted = {right_sorted}')

    # merge the two sorted parts
    merged_result = merge_sorted_arrays(left_sorted, right_sorted)
    # print(f'merged results: {merged_result}')
    return merged_result


def merge_sorted_arrays(A, B):
    '''
        Interleave els from the 2 sorted inputs A and B into 1 combined result array
            + the smaller of A[i] and B[j] goes first into sorted result
    '''

    if not A or not B:
        return A + B

    A_len = len(A)
    B_len = len(B)

    i = 0
    j = 0
    result = []
    while i < A_len and j < B_len:
        if A[i] <= B[j]:
            # B is the anchor part
            # make the larger el the anchor
            # put smaller el in result
            # roam over the non-anchor part: A (the i's)
            result.append(A[i])
            i += 1
        elif A[i] > B[j]:
            # A is the anchor part
            # roam over the non-anchor part: B (the j's)
            result.append(B[j])
            j += 1

    # return the explicit merge PLUS REMAINING RESIDUALS from either A or B
    return result + A[i:] + B[j:]


if __name__ == "__main__":

    inputs = [15, 2, 1, 100, 65, 40, 37, 34]
    inputs2 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    inputs3 = [6, 5, 3, 1, 8, 7, 2, 4]

    print("MERGE SORT RECURSIVELY ...")
    print(f'inputs: {inputs}')
    print(f'sorted: {sort_merge_recursive(inputs)}')

    print(f'inputs: {inputs2}')
    print(f'sorted: {sort_merge_recursive(inputs2)}')

    print(f'inputs: {inputs3}')
    print(f'sorted: {sort_merge_recursive(inputs3)}')
