# Create a Binary Search Algorithm that takes in an a list of values, and a
# value to search for. Return the index of that values first instance if
# found and -1 if not
def binary_search(array, value):

    l = 0
    r = len(array) - 1

    while l <= r:
        m = int((l+r) / 2)

        if array[m] < value:
            l = m + 1
        elif array[m] > value:
            r = m - 1
        else:
            return m
    return -1
