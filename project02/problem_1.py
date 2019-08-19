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
        s = "---LRU Cache Details---\n"
        s += "--- Dict ---\n"
        for k, v in self.cache.items():
            s += "Key: {} Ref: {}\n".format(k, v)
        s += "--- DLL ---\n"
        s += str(self.dll)
        return s


class Node:
    def __init__(self, key, value):

        self.key = key
        self.value = value
        self.prev = None
        self.next = None


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
        self.remove(node)
        return new_node

    # Least recently used node at head
    def popleft(self):
        """Pops an element from head of DLL

        This function is used to get the least recently used element
        """
        if self.head is None:
            return None
        else:
            if self.head != self.tail:
                node = self.head
                self.head = self.head.next
                self.head.prev = None
                return node
            else:
                node = self.head
                self.head = self.tail = None
                return node

    def remove(self, node):

        if self.head and self.tail is None:
            return
        elif node is self.head:
            self.head = self.head.next
            self.head.prev = None
            return
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        else:
            node_before = node.prev
            node_after = node.next

            node_before.next = node_after
            node_after.prev = node_before

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
our_cache.set(4, "nuts")
print(our_cache)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # reurns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

print(our_cache)
our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache)
print(our_cache.get(3))
print(our_cache)
