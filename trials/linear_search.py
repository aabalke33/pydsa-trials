# Sort the array and return the first index of the value if found
# If the value is not found return -1
def linear_search(array, value):
    for i, v in enumerate(array):
        if value == v: return i
    return -1
