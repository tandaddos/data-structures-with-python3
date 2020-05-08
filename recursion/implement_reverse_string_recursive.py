def reverse_string_iterative(mystring):
    '''
        python strings are immutable
        so have to convert them to mutable list
    '''
    reversed = list(mystring)

    full_len = int(len(reversed))
    half_len = int(len(reversed) / 2)

    # the loop does not touch the 'middle' char when the
    # mystring is of odd length
    for i in range(half_len):
        tmp = reversed[i]
        reversed[i] = reversed[full_len - 1 - i]
        reversed[full_len - 1 - i] = tmp

    # note that the 'middle' char is preserved when mystring is of odd length
    return ''.join(reversed)


def reverse_string_recursive(astring):
    '''
        python strings are immutable
    '''
    full_len = int(len(astring))
    half_len = int(full_len / 2)
    if full_len < 2:
        return astring
    elif full_len == 2:
        reversed = list(astring)
        reversed[0], reversed[1] = reversed[1], reversed[0]
        return ''.join(reversed)
    else:

        left_side = astring[:half_len]
        right_side = astring[half_len:]

        reversed_left = reverse_string_recursive(left_side)
        reversed_right = reverse_string_recursive(right_side)
        return reversed_right + reversed_left


if __name__ == "__main__":
    oddlen_string = '01234'
    evenlen_string = '0123456'

    samples = ['hi', 'there', 'once upon a time', 'abracadabra']
    palindromes = ['I did, did I?', 'A dog, a plan, a canal: pagoda',
                   'Was it a car or a cat I saw?'
                   ]

    print(f'REVERSE A STRING ITERATIVELY ...')
    print(f' {oddlen_string} ==> {reverse_string_iterative(oddlen_string)}')
    print(f' {evenlen_string} ==> {reverse_string_iterative(evenlen_string)}')
    for s in samples:
        print(f' {s} ==> {reverse_string_recursive(s)}')

    print(f'REVERSE A STRING RECURSIVELY ...')
    print(f' {oddlen_string} ==> {reverse_string_recursive(oddlen_string)}')
    print(f' {oddlen_string} ==> {reverse_string_recursive(evenlen_string)}')
    mylist = palindromes
    mylist.extend(samples)
    for s in mylist:
        print(f' {s} ==> {reverse_string_recursive(s)}')
