---
title: "Active Directory - Explanation"
author: [Amanuel Gebreweldi]
keywords: [Markdown, Udacity]
---
# Active Directory - Explanation

The Active Directory problem was implemented by iterating recursively a hierarchical tree structure. For this problem, we assume a cyclic nesting group is not part of the requirement as there was no mention of it. 

## Time and Space Complexity
The time complexity is $O(n)$, where `n` is the number of groups.
The space complexity is a little bit tricky, but depends on the maximum depth of the recursion tree generated. All in all, it is $O(gm)$, where `g` is the number of groups and `m` is the maximum depth of the recursion tree.


