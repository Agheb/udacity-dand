import collections


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        if cur_head is None:
            return "Linked List has no elements"

        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):

    # Dictionary that will store the elements of th
    dict_res = collections.defaultdict(int)
    result = LinkedList()
    list_head = llist_1.head

    while list_head:
        dict_res[list_head.value] += 1
        list_head = list_head.next

    list_head = llist_2.head

    while list_head:
        dict_res[list_head.value] += 1
        list_head = list_head.next

    for key in dict_res:
        result.append(key)

    return result


def intersection(llist_1, llist_2):

    # Dictionary that will store the elements of th
    dict_res = collections.defaultdict(int)
    result = LinkedList()
    list1_head = llist_1.head
    list2_head = llist_2.head

    # handle case if second arg has more elements than first
    if llist_2.size() > llist_1.size():
        list1_head, list2_head = list2_head, list1_head

    # Iterate over smaller list
    while list1_head:
        dict_res[list1_head.value] += 1
        list1_head = list1_head.next

    while list2_head:
        # only add to result if key already exists
        if list2_head.value in dict_res:
            if dict_res[list2_head.value] != -1:
                # set count to -1 to avoid duplicates
                dict_res[list2_head.value] = -1
                result.append(list2_head.value)

        list2_head = list2_head.next

    return result


# Test case 1
print("Test Case 1:")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_10 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_3 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_10:
    linked_list_1.append(i)

for i in element_3:
    linked_list_2.append(i)

print("Union Result: " + str(union(linked_list_1, linked_list_2)))
print("Intersection Result " + str(intersection(linked_list_1, linked_list_2)))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
# {4, 21, 6}

# Test case 2

print("Test Case 2:")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Union Result: " + str(union(linked_list_3, linked_list_4)))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->a
print("Intersection Result " + str(intersection(linked_list_3, linked_list_4)))
# None


print("Test Case 3:")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Union Result: " + str(union(linked_list_3, linked_list_4)))
print("Intersection Result: " + str(intersection(linked_list_3, linked_list_4)))
"""
Union Result: Linked List has no elements
Intersection Result: Linked List has no elements
"""
