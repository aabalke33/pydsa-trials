from trials.bubble_sort import bubble_sort

array = [9, 3, 7, 4, 69, 420, 42]

def test():
    if bubble_sort(array) != [3, 4, 7, 9, 42, 69, 420]:
        raise Exception("Bubble Sort Test Failed")
    else:
        print("Bubble Sort Test Passed")
