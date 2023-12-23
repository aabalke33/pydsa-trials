from trials.binary_search import binary_search 

array = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]

def test():
    if ((binary_search(array, 69) != 3) or
        (binary_search(array, 1136) != -1) or
        (binary_search(array, 69420) != 10) or
        (binary_search(array, 69421) != -1) or
        (binary_search(array, 1) != 0) or
        (binary_search(array, 0) != -1)):

        raise Exception("Binary Search Test Failed")
    else:
        print("Binary Search Test Passed")
