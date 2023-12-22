# Quick Sort the inputed array and return the array sorted
def quick_sort(array):

    if len(array) < 2: return array

    p = int(len(array) / 2)
    low = []
    high = []

    for i, value in enumerate(array):
        if value > array[p]:
            high.append(value)
        if value < array[p]:
            low.append(value)
        if value == array[p] and i != p:
            low.append(value)

    p_val = [array[p]]
    low = quick_sort(low)
    high = quick_sort(high)

    return low + p_val + high

