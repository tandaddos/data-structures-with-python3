import sys

# given an array, find first recurring element in array

# loop thru given array:
#   - compute hash of elem H(elem)
#   - if H(elem) already exists in arr_of_hashes, return elem
# at end of loop, return undefined


def find_recurring_elem(arr_in):
    arr_of_hashes = []
    for elem in arr_in:
        hash_of_el = hash(elem)
        if hash_of_el in arr_of_hashes:
            return elem
        else:
            arr_of_hashes.append(hash_of_el)
    return None


if __name__ == "__main__":
    arr_in_1 = [2, 5, 1, 2, 3, 5, 1, 2, 4]
    arr_in_2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
    arr_in_3 = [2, 3, 4, 5]
    arr_in_4 = [1, 5, 5, 1, 3, 4, 6]
    arr_in_5 = [2, 5, 5, 2, 3, 5, 1, 2, 4]

    elem = find_recurring_elem(arr_in_5[:])
    if elem:
        print(f'found {elem}')
    else:
        print(f'no recurring element found')
