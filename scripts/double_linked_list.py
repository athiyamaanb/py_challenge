class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class double_linked_list:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def print_reverse(self):
        temp = self.tail
        while temp:
            print(temp.value)
            temp = temp.prev

    def append(self, value):
        new_node = Node(value)

        temp = self.tail
        temp.next = new_node
        self.tail = new_node
        self.tail.prev = temp
        self.length +=1

    def pop(self):
        temp = self.tail.prev
        temp.next = None
        self.tail = temp
        self.length -=1

    def prepend(self, value):
        new_node = Node(value)
        temp = self.head
        new_node.next = temp
        temp.prev = new_node
        self.head = new_node
        self.length +=1

    def pop_first(self):
        temp = self.head.next
        self.head = temp
        self.head.prev = None
        self.length -=1

    def get(self, index):
        temp = self.head
        for i in range(1, self.length+1):
            if i == index:
                print(temp.value)
                return temp
            temp = temp.next

    def set(self, index, value):
        temp = self.head
        for i in range(1, self.length+1):
            if i == index:
                temp.value = value
            temp = temp.next

    def insert(self, index, value):
        new_node = Node(value)
        temp = self.head
        for i in range(1, self.length+1):
            if i == index:
                before = temp.prev
                after = temp

                before.next = new_node
                new_node.prev = before

                after.prev = new_node
                new_node.next = after

                self.length += 1
                return
            temp = temp.next

    def remove(self, index):
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1


dll = double_linked_list(11)

dll.append(22)
dll.append(33)
dll.append(44)
# dll.print()
# dll.print_reverse()
dll.pop()
# dll.print()
# dll.print_reverse()
dll.prepend(-11)

dll.pop_first()


# dll.get(2)

# dll.set(2, 2222)

dll.insert(2,1000)
dll.print()
dll.remove(2)
dll.print()
# dll.print_reverse()
# dll.get(2)
