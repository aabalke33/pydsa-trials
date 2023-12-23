# Build a Queue class using Nodes for each element
# Python Lists should not be used to create the Queue
# Node Class Should have a Constructor
# Queue Class Should have a Constructor and enqueue, deque and peek methods
class Node:
    def __init__(self, value=None, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, item):
        self.length += 1
        node = Node(item)

        if self.tail:
            self.tail.next = self.tail = node
        else:
            self.head = self.tail = node

    def deque(self):
        if self.head and self.length:
            self.length -= 1
            head = self.head
            self.head = head.next

            if not self.length: self.tail = None

            return head.value

    def peek(self):
        if self.head:
            return self.head.value
