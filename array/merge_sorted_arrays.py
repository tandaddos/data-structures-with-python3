def merge_sorted_arrays(ar1, ar2):
    """
    Function: merge_sorted_arrays
    Summary: InsertHere
    Examples: InsertHere
    Attributes: 
        @param (ar1):InsertHere
        @param (ar2):InsertHere
    Returns: InsertHere
    """
    if not ar1 or not ar2:
        return ar1 + ar2

    ar1_len = len(ar1)
    ar2_len = len(ar2)

    merged = []
    i = 0
    j = 0

    while i < ar1_len and j < ar2_len:
        if ar1[i] <= ar2[j]:
            merged.append(ar1[i])
            i += 1
        else:
            merged.append(ar2[j])
            j += 1

    # return the explicit merge plus remaining residuals from either ar1 or ar2
    return merged + ar1[i:] + ar2[j:]


a = [0, 3, 4, 31]
b = [4, 6, 30]

c = [1, 2, 3, 4]
d = [3, 7, 9, 12]
e = []
print(f"{merge_sorted_arrays(a, b)}")
print(f"{merge_sorted_arrays(a, e)}")
