class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    # def append(self, value):
    #
    # def prepend(self, value):
    #
    # def insert(self, index, value):


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def pop_mine(self):
        if self.length == 0:
            print('List is empty')
            return None

        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length +=1


    def pop_first(self):
        self.head = self.head.next
        self.length -= 1


    def get(self, index):
        temp = self.head
        i = 1
        while i <= self.length:
            if i == index:
                print(temp.value)
            i +=1
            temp = temp.next


    def set(self, index, value):
        temp = self.head
        i = 1
        while i <= self.length:
            if i == index:
                temp.value = value
            i +=1
            temp = temp.next

    def insert(self, index, value):
        new_node = Node(value)
        temp = self.head
        pre = self.head
        i = 1
        while i <= self.length:
            if i == index:
                self.length +=1
                new_node.next = pre.next
                pre.next = new_node

                return True
            i += 1
            pre = temp
            temp = temp.next


    def remove(self, index):
        temp = self.head
        pre = self.head
        i = 1
        while i<= self.length :
            if i == index:
                pre.next = temp.next
                self.length -=1
                return True
            i +=1
            pre = temp
            temp = temp.next

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        # after = temp.next
        before = None

        for i in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

# print(my_linked_list.head.value)
# print(my_linked_list.tail.value)
# my_linked_list.print_list()
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.print_list()

# print('----')
# print(my_linked_list.pop_mine())
# print('----')
# print(my_linked_list.pop_mine())
# print('----')
# print(my_linked_list.pop_mine())
# print('----')
# print(my_linked_list.pop_mine())
# print('----')
# my_linked_list.print_list()
print('----')
my_linked_list.prepend(9)
my_linked_list.print_list()
print('----')
my_linked_list.prepend(8)
my_linked_list.print_list()
# print('----')
# my_linked_list.pop_first()
# my_linked_list.print_list()
# print('----')
# my_linked_list.pop_first()
# my_linked_list.print_list()

print('----')
my_linked_list.get(2)

print('----')
my_linked_list.set(2,888)
my_linked_list.print_list()

print('----')
my_linked_list.insert(3,777)
my_linked_list.print_list()

my_linked_list.insert(4,666)
my_linked_list.print_list()


print('----')
my_linked_list.remove(4)
my_linked_list.print_list()

print('----')
my_linked_list.remove(3)
my_linked_list.print_list()

print('----')
my_linked_list.reverse()
my_linked_list.print_list()
