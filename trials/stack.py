# Build a Stack class using Nodes for each element
# Python Lists should not be used to create the Stack
class Node:
    def __init__(self, value=None, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev

class Stack:
    def __init__(self) -> None:
        self.length = 0
        self.head = None

    def push(self, item):
        self.length += 1
        node = Node(item)

        if self.head:
            node.prev = self.head
            self.head = node
        else:
            self.head = node

    def pop(self):
        if self.head and self.length:
            self.length -= 1
            head = self.head
            self.head = head.prev
            return head.value

    def peek(self):
        if self.head:
            return self.head.value
