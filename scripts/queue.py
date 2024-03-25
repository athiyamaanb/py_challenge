
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        self.last.next = new_node
        self.last = new_node
        self.length += 1

    def dequeue(self):
        temp = self.first.next
        self.first = temp
        self.length -= 1

my_queue = Queue(1)
my_queue.print()


my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.print()

print('-----')

my_queue.dequeue()
my_queue.print()
my_queue.enqueue(5)

print('-----')

my_queue.dequeue()
my_queue.print()