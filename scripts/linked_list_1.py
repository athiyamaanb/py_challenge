class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
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

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length +=1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop(self):
        temp = self.head
        i = 1
        while i < self.length -1:
            temp = temp.next
            i +=1

        self.tail = temp
        temp.next = None

        self.length -= 1

    def pop_first(self):
        temp = self.head
        self.head = temp.next
        self.length -= 1

    def get(self, index):
        temp = self.head
        i = 1
        while i <= self.length:
            if index == i:
                print(temp.value)
            temp = temp.next
            i +=1

    def set(self, index, value):
        temp = self.head
        i = 1
        while i <= self.length:
            if index == i:
                temp.value = value
            temp = temp.next
            i +=1


    def insert(self, index, value):
        new_node = Node(value)
        temp = self.head
        i = 1
        while temp:
            if index == i:
                v = temp.next
                temp.next = new_node
                new_node.next = v
                self.length +=1
                break
            i +=1
            temp = temp.next


    def remove(self, index):
        temp = self.head
        prev = self.head
        i = 1
        while temp:
            if index == i:
                prev.next = temp.next
                self.length -=1
                break
            prev = temp
            temp = temp.next
            i +=1


    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = None
        before = None
        for i in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


linkedList = LinkedList(222)

linkedList.append(333)
linkedList.append(6666)
linkedList.prepend(111)
linkedList.prepend(000)
linkedList.prepend(-1)
linkedList.print()
print('----')
linkedList.pop()
linkedList.pop()
linkedList.print()
print('----')
linkedList.pop_first()
linkedList.print()

print('----')
linkedList.get(3)

print('----')
linkedList.set(1,999)
linkedList.print()


print('----')
linkedList.insert(2,-100)
linkedList.insert(3,-900)
linkedList.print()

print('----')
linkedList.remove(4)
linkedList.remove(3)
linkedList.print()


print('----')

# print(linkedList.length)
# print(linkedList.head.value)
# print(linkedList.tail.value)\
linkedList.reverse()
linkedList.print()