def sort_insertion_not_in_place(arr):
    '''
        input list = [ a(0), a(1), a(2), ..... a(n-1)]

        return a new sorted list 

        algo =
            working_list = []
            for index in input list:
                put a[index] in to working_list at correct location
                    + correct location in working_list may be:
                        * at the start
                        * somewhere in middle
                        * at the end
                    + comparison =
                        * smaller element goes to the left

        this algo builds up the sorted working_list one element at a time
    '''
    working_list = []
    for el in arr:
        if len(working_list) == 0:
            # populate working list with first item
            working_list.append(el)
        else:
            '''
                Figure out where to add new item to non-empty working list
                    - in the middle: use insert()
                    - at the end: use append()
            '''
            new_append_new_entry = True
            for i, v in enumerate(working_list):
                if el < v:
                    working_list.insert(i, el)
                    new_append_new_entry = False
                    break
            if new_append_new_entry:
                # 'el' is larger than any item in working_list --> append 'el'
                working_list.append(el)

    return working_list


def sort_insertion_in_place(arr):
    '''
        sort in place

        algo = 
            construct in place a partially sorted sublist from original input list
                - this sublist builds from the start of original input list
            the order in the sublist is low to high, from left to right
            comparison is made between successive elements in original list to elements in sublist

        sort in place is harder because have to:
            - keep track of the sublist (its start and end)
            - as well as where we are in the original input list
            - during construction of sublist, remember to exclude the element (in original list)
                that is being compared
    '''
    for i, v in enumerate(arr):

        # v is the el in input list under examination/comparison
        # its index is always immediately to the right of the end of the sublist
        # print(f'(i,v) = ({i},{v})')

        if v < arr[0]:
            # put this el[i] at the front of sublist
            # <v> <start of sublist to just before v> <after v to end of input list>
            arr[:] = arr[i: i+1] + arr[:i] + arr[i+1:]
            # print(f' added to front of sublist: {arr}')

        elif v > arr[i-1]:
            # add el[i] at end of sublist
            # <all of current sublist> <v> <after v to end of input list>
            arr[:] = arr[:i] + arr[i:i+1] + arr[i+1:]
            # print(f'added to end of sublist: {arr}')
        else:
            for j in range(i):
                if arr[j] < v and v < arr[j+1]:
                    # insert v in middle of sublist, between low_el and high_el
                    # <start of sublist to low_el>
                    #   <v>
                    #   <from sublist high_el to end of sublist>
                    #   <after v to end of input list>
                    arr[:] = arr[:j+1] + arr[i:i+1] + arr[j+1:i] + arr[i+1:]
                    # print(f'added to middle of sublist: {arr}')
                    break


if __name__ == "__main__":

    inputs = [15, 2, 1, 100, 65, 40, 37, 34]
    inputs2 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    inputs3 = [6, 5, 3, 1, 8, 7, 2, 4]

    print("SELECTION SORT (NOT IN PLACE)...")
    print(f'inputs: {inputs}')
    print(f'sorted: {sort_insertion_not_in_place(inputs)}')

    print(f'inputs: {inputs2}')
    print(f'sorted: {sort_insertion_not_in_place(inputs2)}')

    print(f'inputs: {inputs3}')
    print(f'sorted: {sort_insertion_not_in_place(inputs3)}')

    print("SELECTION SORT IN PLACE...")
    '''
        sort_insertion_in_place() sorts in place 
        it does not return any result, so have to print separately
    '''
    print(f'inputs: {inputs}')
    sort_insertion_in_place(inputs)
    print(f'inputs: {inputs}')

    print(f'inputs: {inputs2}')
    sort_insertion_in_place(inputs2)
    print(f'inputs: {inputs2}')

    print(f'inputs: {inputs3}')
    sort_insertion_in_place(inputs3)
    print(f'inputs: {inputs3}')
