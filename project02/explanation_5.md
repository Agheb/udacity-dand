---
title: "Blockchain - Explanation"
author: [Amanuel Gebreweldi]
keywords: [Markdown, Udacity]
---
# BlockChain - Explanation

For this problem, the blockchain was implemented using a Linked List. 
Note that, we still need to use a pointer called `ref` to refer to elements in the linked list implementation. In Python, this hash is set by default and corresponds to its position in memory. 
We could create our own hashable objects based on `previous_hash` but this might be too advanced for this project.

## Time Complexity and Space Complexity
The time complexity to print the chain, is $O(n)$ with n the numbers of blocks. The time complexity for adding a new block is $O(1)$, because new nodes are added at the front of the linked list.
The space complexity is $O(n)$, where n is the number of blocks.