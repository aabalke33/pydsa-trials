from trials.stack import Stack

def test():
    stack = Stack()

    stack.push(5)
    stack.push(7)
    stack.push(9)

    if stack.pop() != 9: raise Exception("Stack Implimentation Failed")
    if stack.length != 2: raise Exception("Stack Implimentation Failed")

    stack.push(11)

    if stack.pop() != 11: raise Exception("Stack Implimentation Failed")
    if stack.pop() != 7: raise Exception("Stack Implimentation Failed")
    if stack.peek() != 5: raise Exception("Stack Implimentation Failed")
    if stack.pop() != 5: raise Exception("Stack Implimentation Failed")
    if stack.pop() != None: raise Exception("Stack Implimentation Failed")

    stack.push(69)
    if stack.peek() != 69: raise Exception("Stack Implimentation Failed")
    if stack.length != 1: raise Exception("Stack Implimentation Failed")

    print("Stack Implimentation Passed")
