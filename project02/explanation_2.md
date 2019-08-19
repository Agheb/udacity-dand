---
title:      "File Recursion - Explanation"
author:     [Amanuel Gebreweldi]
keywords:   [Markdown,Udacity]
---

# File Recursion 

The solution is divided up in two components:
- ```_find_files(...)```, which is a generator function  
- ```find_files(...)```  

The generator function ```_find_files()``` first uses ```link_dir()


In the parent function, we need to return a list of the paths.
As required, we can do this in an one-liner that turns the generator expression into a list:
```python
return list(_find_files(suffix, parents))
```
