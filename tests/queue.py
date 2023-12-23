from trials.queue import Queue

def test():

    queue = Queue()

    queue.enqueue(5)
    queue.enqueue(7)
    queue.enqueue(9)

    if queue.deque() != 5: raise Exception("Queue Implimentation Failed")
    if queue.length != 2:  raise Exception("Queue Implimentation Failed")

    queue.enqueue(11)

    if queue.deque() != 7: raise Exception("Queue Implimentation Failed")
    if queue.deque() != 9: raise Exception("Queue Implimentation Failed")
    if queue.peek() != 11: raise Exception("Queue Implimentation Failed")
    if queue.deque() != 11: raise Exception("Queue Implimentation Failed")
    if queue.deque() != None: raise Exception("Queue Implimentation Failed")
    if queue.length != 0: raise Exception("Queue Implimentation Failed")

    queue.enqueue(69)

    if queue.peek() != 69: raise Exception("Queue Implimentation Failed")
    if queue.length != 1: raise Exception("Queue Implimentation Failed")

    print("Queue Implimentation Passed")
