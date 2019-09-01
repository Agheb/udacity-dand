#!/usr/bin/env python3
class LRU_Cache:
    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {}
        self.dll = DLL()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.cache:
            return -1
        else:
            self.dll.move_to_tail(self.cache[key])
            return self.cache[key].value

    def set(self, key, value):
        """ Set the value if the key is not present in the cache.

        If the cache is at capacity remove the oldest item.
        """
        if key in self.cache:
            new_node = self.dll.move_to_tail(self.cache[key])
            self.cache[key] = new_node
        else:

            if len(self.cache) >= self.capacity:

                lru_item = self.dll.popleft()
                del self.cache[lru_item.key]

            node = self.dll.insertion_at_tail(key, value)
            self.cache[key] = node

    def __str__(self):
        s = "---LRU Cache ---\n"
        s += str(self.dll)
        s += "---------------\n"
        return s


class Node:
    def __init__(self, key, value):

        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return f"{self.value}"


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    # Most recently used  at tail
    def insertion_at_tail(self, key, value):
        """Insert kv store as node in doubly linked list(DLL) at tail

        This function is used to add the most recently used value at tail of DLL and to return
        the created node
        """
        d_node = Node(key, value)

        if self.head is None:
            self.head = d_node
            self.tail = self.head
            return self.tail

        self.tail.next = d_node
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        return self.tail

    def move_to_tail(self, node):
        """Moves any existing node reference to tail of DLL and deletes the old one for safe-keeping. 

        This function is used when an element is retrieved from cache with a get call. 
        """
        new_node = self.insertion_at_tail(node.key, node.value)
        self.popleft()
        return new_node

    # Least recently used node at head
    def popleft(self):
        """Pops an element from head of DLL

        This function is used to remove and return the least recently used element
        """
        if self.head is None:
            return None
        else:
            if self.head is not self.tail:
                node = self.head
                self.head = self.head.next
                self.head.prev = None
                return node
            else:
                node = self.head
                self.head = self.tail = None
                return node

    def __str__(self):
        node = self.head
        if self.head is None:
            return "DLL is empty"
        s = ""
        while node is not None:
            s += "Key: {} Val: {}\n".format(node.key, node.value)
            node = node.next

        return s


our_cache = LRU_Cache(5)

our_cache.set(1, "apple")
our_cache.set(2, "banana")
our_cache.set(3, "strawberry")
print(our_cache)
"""
---LRU Cache ---
Key: 1 Val: apple
Key: 2 Val: banana
Key: 3 Val: strawberry
---------------
"""

our_cache.set(4, "nuts")
our_cache.set(5, "bogus")
print(our_cache)
"""
Key: 1 Val: apple
Key: 2 Val: banana
Key: 3 Val: strawberry
Key: 4 Val: nuts
Key: 5 Val: bogus
"""

our_cache.get(1)
our_cache.get(2)
our_cache.get(3)
print(our_cache)
"""
Key: 4 Val: nuts
Key: 5 Val: bogus
Key: 1 Val: apple
Key: 2 Val: banana
Key: 3 Val: strawberry
"""

our_cache.set(6, "jackfruit")
our_cache.set(7, "oranges")
print(our_cache)
"""
Key: 1 Val: apple
Key: 2 Val: banana
Key: 3 Val: strawberry
Key: 6 Val: jackfruit
Key: 7 Val: oranges
"""

our_cache.set(8, "blueberries")
print(our_cache)
"""
Key: 2 Val: banana
Key: 3 Val: strawberry
Key: 6 Val: jackfruit
Key: 7 Val: oranges
Key: 8 Val: blueberries
"""
