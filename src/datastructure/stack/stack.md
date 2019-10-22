# Stack

## What is it?
```
A data structure that stores values using a Last In First Out (LIFO) process.

Like a stack of dishes, in order to access the bottom-most dish, all other dishes on top must be moved first. 

This implementation uses a Singly Linked List (and nodes) and accepts a value to determine maximum stack size.

Alternative implementations:
 - Array
```

## Common functions
### push: O(1)

### pop: O(1)

### peek: O(1)

### is_empty: O(1)

## Where and/or when is it used?
```
1. Cafeteria trays where new trays pop up when the top is removed.
2. DFS algorithm
3. Browser back-forward button
4. Word processor: undo and redo actions

```

## Time and Space Complexity
```
Extra pointers are used for the head, stack size, and count of items in the stack.
Space:
n = number of nodes
O(n)
```