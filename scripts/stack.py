
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1

    def pop(self):
        temp = self.top
        self.top = temp.next
        self.height -= 1


my_stack = Stack(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.print()

my_stack.pop()
my_stack.pop()
my_stack.print()

