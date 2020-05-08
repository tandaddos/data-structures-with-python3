def sort_selection(arr):
    '''
        input list = [ a(0), a(1), a(2), ..... a(n-1)]

        input list is sorted in place

        algo =
            for index in input list:
                anchor = index

                index_of_smallest_found = anchor
                smallest_found = a[anchor]

                loop:
                    scan through rest of input list:
                        + to find smallest and index_of_smallest_found

                    swap a[anchor] = a[index_of_smallest_found]

                repeat above loop to find the next smallest el to fill in at the anchor index

        this algo pushes the smallest to the left
    '''

    n = int(len(arr))
    for anchor in range(n):
        index_of_smallest_found = anchor
        for i in range(anchor+1, n):
            if arr[i] < arr[index_of_smallest_found]:
                index_of_smallest_found = i

        # swap els at anchor and at index_of_smallest_found
        arr[anchor], arr[index_of_smallest_found] = \
            arr[index_of_smallest_found], arr[anchor]


if __name__ == "__main__":
    print("SELECTION SORT ...")
    inputs = [15, 2, 1, 100, 65, 40, 37, 34]
    inputs2 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

    print(f'inputs: {inputs}')
    sort_selection(inputs)
    print(f'sorted: {inputs}')

    print(f'inputs: {inputs2}')
    sort_selection(inputs2)
    print(f'sorted: {inputs2}')
