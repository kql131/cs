# Trie

## What is it?
```
A tree like structure that consists of Nodes. 

Each node has a value in the alphabet that also contains a reference to another Node.
```

## Common functions

### find: O(n)
```
Because find() returns all of the words given some letters, ex: 'ca', all paths must be traversed after 'ca' to look for words that begin with 'ca'.
If the Trie contained ['catch', 'call', 'caller', 'can', 'do'], passing in 'ca', should return all words 4 words.
```

### insert: O(n)
```
n = length of string being inserted
```

## Usage
```
Search engines and long URL mappings.
```

Time and Space complexity
```
Nodes are implemented with a dictionary to represent its children.
Only the 26 alphabet characters ('A-Z' and 'a-z') are used as keys.

The Trie itself is implemented with a pointer to a head null node.

Space (Trie): 
N = number of nodes
K = references
O(N * K)
```
