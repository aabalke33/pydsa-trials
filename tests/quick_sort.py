from trials.quick_sort import quick_sort
array = [9, 3, 7, 4, 69, 420, 42]

def test():
    if quick_sort(array) != [3, 4, 7, 9, 42, 69, 420]:
        raise Exception("Linear Search Test Failed")
    else:
        print("Linear Search Test Passed")
