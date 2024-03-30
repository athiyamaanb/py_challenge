class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node

    def insert(self, value):
        temp = self.root
        new_node = Node(value)
        while temp:
            if value == temp.value:
                return False
            elif value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right



my_tree = BinarySearchTree(36)
my_tree.insert(12)
my_tree.insert(40)
my_tree.insert(7)

print(my_tree.root.value)

print(my_tree.root.left.value)
print(my_tree.root.right.value)