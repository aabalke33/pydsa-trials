from tests.linear_search import test as linear_search
from tests.binary_search import test as binary_search
from tests.quick_sort import test as quick_sort
from tests.bubble_sort import test as bubble_sort
from tests.queue import test as queue
from tests.stack import test as stack

if __name__ == "__main__":
    welcome = '''
        Welcome to the PyDSA Trials!
        A small app to test your DSA abilities in Python.
        The trials folder will provide files to impliment algorithms.
        When you have completed your implimentation and are ready to evaluate
        Come back here and choose the test your want to run.
        Choose one of the following Algorithms:

        Searches:
        [a]   Linear Search
        [b]   Binary Search
        
        Sorts:
        [c]   Bubble Sort
        [d]   Quick Sort
        [e]   Merge Sort
        [f]   Insertion Sort

        Data Structures
        [g]   ArrayList
        [h]   Linked List
        [i]   Doubley Linked List
        [j]   Queue
        [k]   Stack
        '''

    print(welcome)
    chosen = input("\tOption: ")

    match chosen:
        case "a": linear_search()
        case "b": binary_search()
        case "c": bubble_sort()
        case "d": quick_sort()

        case "j": queue()
        case "k": stack()
        case _:
            print("Invalid Option")
