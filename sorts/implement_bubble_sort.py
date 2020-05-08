def sort_bubble(arr):
    '''
        input list = [ a(0), a(1), a(2), ..... a(n-1)]

        input list is sorted in place

        algo =
            for index in inputlist
                compare a[i] and a[i+1]. Put lowest in a[i]
                    ==> this pushes the larger of the 2 els towards the right
                    ==> eventually the largest el gets pushed to the end
            repeat above loop to get next largest
                eventually, above for loop is repeated n times for n els

        this algo pushes the largest to the right

    '''

    n = int(len(arr))
    for m in range(n):
        ''' 
            the m loop executes n times to get n numbers in order
            the i loop executes (n-m) times because fewer comparisons are needed:
                + 1st time: make n-1 compares
                + 2nd time: already found largest, make n-2 compares
        '''

        for i in range(n-m):
            '''
                loop from 1st el to last el
                    we compare el[i] and el[i+1]
                    for last el: i = (n-1) so el[i+1] = el[n] does not exist
                    so stop when i = (n-2)
                range(n) yields 0 .. (n-2) (n-1)
            '''
            if i == n - 1:
                # reached the last
                break

            # print(f' ({arr[i]}, {arr[i+1]})')
            if arr[i] > arr[i+1]:
                # swap - put larger element to the right
                arr[i], arr[i+1] = arr[i+1], arr[i]


if __name__ == "__main__":
    print("BUBBLE SORT ...")
    inputs = [15, 2, 1, 100, 65, 40, 37, 34]
    inputs2 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

    print(f'inputs: {inputs}')
    sort_bubble(inputs)
    print(f'sorted: {inputs}')

    print(f'inputs: {inputs2}')
    sort_bubble(inputs2)
    print(f'sorted: {inputs2}')
