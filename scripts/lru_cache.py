class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, key, value, capacity):
        self.cache = {}
        self.capacity = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.right, self.right.left = self.right, self.left

    def remove(self, node):


    def get(self, key):

        return


    def put(self, key, value):


        return

lru_cache = LRUCache(1, 'a', 5)

