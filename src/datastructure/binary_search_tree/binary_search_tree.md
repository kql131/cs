# Binary Search Tree

## What is it?

A data structure that stores items in memory, represented by nodes with a key.
Each node has a left subtree (left) and right subtree (right) property.

The tree also follows the binary search property where the key in each node must be greater than the nodes stored in the left subtree and less than or equal to any key stored in the right subtree.

Because the nodes are kept in a sorted order, search, insert, and delete operations can be done, on average, in half of the time relative to the number of nodes in the tree.


## Common functions
### search:
```
n = nodes in the tree
Average: O(log n)
Worst: O(n)
```

### insert:
```
n = nodes in the tree
Average: O(log n)
Worst: O(n)
```

### delete:
```
n = nodes in the tree
Average: O(log n)
Worst: O(n)
```

## Where and/or when is it used?
```
1. Finding the phone number of a person by name in a lookup table.
2. Dyanmic sets or map (if balanced properly)
```

## Time and Space Complexity
```
Space: 
O(n) where n = number of nodes

```