from trials.linear_search import linear_search

array = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]

def test():
    if ((linear_search(array, 69) != 3) or
        (linear_search(array, 1136) != -1) or
        (linear_search(array, 69420) != 10) or
        (linear_search(array, 69421) != -1) or
        (linear_search(array, 1) != 0) or
        (linear_search(array, 0) != -1)):

        raise Exception("Linear Search Test Failed")
    else:
        print("Linear Search Test Passed")
