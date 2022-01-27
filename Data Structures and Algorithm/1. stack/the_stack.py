# The data structure stack is very similar to a physical stack that you’d most likely be familiar with. 
# The stack data structure allows us to place any programming artifact, variable or object on it, 
# just as our example stack allowed us to put books in it.

# stack operation:  push    = place element on top
#                   pop     = put out element on top
#                   peek    = view top element (without removing it)

"""
Stack Data Structure.
"""
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

if __name__ == "__main__":
    myStack = Stack()
    print(myStack.is_empty())
    myStack.push("A")
    myStack.push("B")
    print(myStack.get_stack())
    print(myStack.is_empty())
    myStack.push("C")
    print(myStack.get_stack())
    myStack.pop()
    print(myStack.peek())
    print(myStack.get_stack())