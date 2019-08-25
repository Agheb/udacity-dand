import sys
from queue import PriorityQueue


class Huffman_Node:
    def __init__(self, value, weight, entry_count=0):
        self.left = None
        self.right = None
        self.value = value
        self.weight = weight
        self.entry_count = entry_count

    def __repr__(self):
        return f"Char[{self.value}] - Freq[{self.weight}] - Entry_Count[{self.entry_count}]"

    def __lt__(self, other):
        # If same weight use entry_count as tie breaker
        this_obj = (self.weight, self.entry_count)
        other_obj = (other.weight, other.entry_count)
        return this_obj < other_obj


def huffman_encoding(data):
    # Character frequency in the form of a tuple (priority_number, data)
    freq = [(data.count(e), e) for e in sorted(set(data))]
    root = _build_huffman_tree(freq)

    codes = {}
    _get_codes(root, codes)

    # Encode Data in compressed form
    encoded_data = "".join(codes[n] for n in data)
    return encoded_data


def huffman_decoding(data, tree):
    decoded_txt = []
    root = tree
    for b in data:
        # Visit left children if 0
        if tree.left and b == "0":
            tree = tree.left
        # Visit right children if 1
        elif tree.right:
            tree = tree.right

        # Arrive at Leaf node
        if tree.left is None and tree.right is None:
            decoded_txt.append(tree.value)
            # Return to root to decode next binary number
            tree = root

    return "".join(decoded_txt)


def _build_huffman_tree(char_freq):
    """create Huffman tree using a priority queue

    Keyword argument:
    char_freq -- character frequency list.
    """
    # Add Priority Queue
    q = PriorityQueue()

    # If a pair of chars has same weight, use entry_counter as tie breaker
    # https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes
    entry_count = 0
    for f, v in sorted(char_freq):
        entry_count += 1
        q.put(Huffman_Node(v, f, entry_count))

    # Merge Nodes after weight:
    while q.qsize() > 1:
        n1 = q.get()
        n2 = q.get()
        merge_n = Huffman_Node(None, n1.weight + n2.weight)
        merge_n.left = n1
        merge_n.right = n2
        q.put(merge_n)

    # Get root of huffman tree (remaining node in priority queue)
    root = q.get()
    return root


def _get_tree(data):
    """wrapper function if you only need the tree and not encoded text

    Keyword arguments:
    data -- a string of text to encode
    """
    char_freq = [(data.count(e), e) for e in sorted(set(data))]
    tree = _build_huffman_tree(char_freq)
    return tree


def _get_codes(root, codes, bin_str=""):
    """Traverse recursively to obtain Huffman codes from the Huffman tree


    Keyword arguments:
    root -- root of Huffman tree
    codes -- dict (must be initialized outside of func)
    bin_str -- stores append huffman codes after each
    recursive call(default to "")
    """
    if root is not None:
        if root.value is not None:
            codes[root.value] = bin_str
            return
        else:
            _get_codes(root.left, codes, bin_str + "0")
            _get_codes(root.right, codes, bin_str + "1")


if __name__ == "__main__":

    a_great_sentence = "The bird is the word"

    encoded_data = huffman_encoding(a_great_sentence)

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    print(
        "The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))
        )
    )
    print("The content of the encoded data is: {}\n".format(encoded_data))

    tree = _get_tree(a_great_sentence)

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
