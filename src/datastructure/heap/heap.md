[towardsdatascience.com](https://towardsdatascience.com/data-structure-heap-23d4c78a6962)



# 6 Steps to Understanding a Heap with Python

Yasufumi TANIGUCHI

10-13 minutes

------



## The Important Data Structure for Search Algorithms



[![Yasufumi TANIGUCHI](https://miro.medium.com/fit/c/96/96/1*DJgC5WgpMNqfVeru2NefzA.jpeg)](https://towardsdatascience.com/@yasufumy?source=post_page-----23d4c78a6962----------------------)

Today  I will explain the heap, which is one of the basic data structures.  Also, the famous search algorithms like Dijkstra's algorithm or A* use  the heap. A* can appear in the *Hidden Malkov Model* (HMM) which is often applied to time-series pattern recognition.  Please note that this post isn’t about search algorithms. I’ll explain  the way how a heap works, and its time complexity and Python  implementation. The lecture of MIT OpenCourseWare really helps me to  understand a heap. So I followed the way of explanations in that lecture  but I summarized a little and added some Python implementations. This  post is structured as follow and based on [MIT’s lecture](https://www.youtube.com/watch?v=B7hVxCmfPtM). Let’s get started!

1. Overview of heap
2. Representation
3. The way how to build a heap
4. Time complexity
5. Implementation
6. Heapsort

A heap is one common implementation of [a priority queue](https://en.wikipedia.org/wiki/Priority_queue). A priority queue contains items with some priority. You can always take an item out in the priority order from a priority queue.  It is important to take an item out based on the priority. When you  look around poster presentations at an academic conference, it is very  possible you have set in order to pick some presentations. Or you will  make a priority list before you go sight-seeing (In this case, an item  will be a tourist spot.). A stack and a queue also contain items. You  can take an item out from a stack if the item is the last one added to  the stack. This is first in, last out (FILO). As for a queue, you can  take an item out from the queue if this item is the first one added to  the queue. This is first in, first out (FIFO). You can regard these as a specific type of a priority queue. This is because the priority of an inserted item in stack increases and the priority of an inserted item in a queue decreases.

![img](https://miro.medium.com/max/60/1*oN767xTYckRTUjTIyS3oyw.png?q=20)

![img]()

A heap is one of the tree structures and represented as a binary tree.  I put the image of heap below. You can implement a tree structure by a  pointer or an array. In this post, I choose to use the array  implementation like below. In terms of space complexity, the array  implementation has more benefits than the pointer implementation. The  indices of the array correspond to the node number in the below image.

![img](https://miro.medium.com/max/60/1*ds0JXOw3lLqNo6hw__NtZw.png?q=20)

![img]()

The heap above is called *a min heap*, and **each value of nodes is less than or equal to the value of child nodes****.** We call this condition the heap property.

![img](https://miro.medium.com/max/60/1*MaIob54cy5Z7iL1TAEDt1A.png?q=20)

![img]()

In a min heap, when you look at the parent node and its child nodes, the parent node always has the smallest value. When a heap has an opposite definition, we call it *a max heap*. For the following discussions, we call a min heap a heap.

You can access a parent node or a child nodes in the array with indices below.

- A root node｜*i* = 1, the first item of the array
- A parent node｜parent(*i*) = *i* / 2
- A left child node｜left(*i*) = 2*i*
- A right child node｜right(*i*)=2*i*+1

When you look at the node of index 4, the relation of nodes in the tree corresponds to the indices of the array below.

![img](https://miro.medium.com/max/60/1*ysSV1xV0OMm-1amWBpFb0A.png?q=20)

![img]()

The parent node corresponds to the item of index 2 by parent(*i*) = 4 / 2 = 2. The child nodes correspond to the items of index 8 and 9 by left(*i*) = 2 * 2 = 4, right(*i*) = 2 * 2 + 1 = 5, respectively.

You need two operations to build a heap from an arbitrary array.

1. `min_heapify`｜make some node and its descendant nodes meet the heap property.
2. `build_min_heap`｜produce a heap from an arbitrary array.

We can build a heap by applying *min_heapify* to each node repeatedly.

## 3.1 min_heapify

In *min_heapify*, we exchange some nodes with its child nodes to satisfy the heap property under these two features below;

1. Some node and its child nodes don’t satisfy the heap property,
2. That child nodes and its descendant nodes satisfy the property.

A tree structure has the two features below.

![img](https://miro.medium.com/max/60/1*7GdM58KmWHBgEE-yOSRy4Q.png?q=20)

![img]()

Look  at the nodes surrounded by the orange square. We find that 9 is larger  than both of 2 and 3, so these three nodes don’t satisfy the heap  property (The value of node should be less than or equal to the values  of its child nodes). Please check the orange nodes below.

![img](https://miro.medium.com/max/60/1*iDBRhJGiIyCBIAdVOMQnyg.png?q=20)

![img]()

However, look at the blue nodes. These nodes satisfy the heap property.

![img](https://miro.medium.com/max/60/1*8DJyn5AJMYp4DqWgv0dJAg.png?q=20)

![img]()

Here we define *min_heapify*(*array*, *index*). This method takes two arguments, *array,* and *index*. We assume this method exchange the node of *array*[*index*] with its child nodes to satisfy the heap property.

Let’s check the way how *min_heapify* works by producing a heap from the tree structure above. First, we call *min_heapify*(*array*, 2) to exchange the node of index 2 with the node of index 4.

![img](https://miro.medium.com/max/60/1*6ZsaVxXdLu0fyOz99GD1vg.png?q=20)

![img]()

After apply *min_heapify*(*array*, 2) to the subtree, the subtree changes below and meets the heap property. This subtree colored blue.

![img](https://miro.medium.com/max/60/1*Pg5r3aNAcMluu2YafmcOEw.png?q=20)

![img]()

If  the subtree exchanged the node of index 2 with the node of index5, the  subtree won’t meet the heap property like below. So the subtree exchange  the node has the smallest value in the subtree with the parent node to  satisfy the heap property.

![img](https://miro.medium.com/max/60/1*1MXtFjQWaWTqNTGakj4DNg.png?q=20)

![img]()

Get back to the tree correctly exchanged. When we look at the orange nodes, this subtree doesn’t satisfy the heap property.

![img](https://miro.medium.com/max/60/1*sE-XfLcquAc8u1Xzxe5PmA.png?q=20)

![img]()

So call *min_heapify*(*array*, 4) to make the subtree meet the heap property.

![img](https://miro.medium.com/max/60/1*NGqt-gG64O_X1GJei_MdJQ.png?q=20)

![img]()

Now, this subtree satisfies the heap property by exchanging the node of index 4 with the node of index 8.

These operations above produce the heap from the unordered tree (the array).

## 3.2 build_min_heap

The pseudo-code below stands for how *build_min_heap* works.

```
build_min_heap(array)
    for i=n/2 downto 1
        do min_heapify(array, i)
```

This function iterates the nodes except the leaf nodes with the for-loop and applies *min_heapify* to each node. We don’t need to apply *min_heapify* to the items of indices after *n*/2+1, which are all the leaf nodes. We apply *min_heapify in* the orange nodes below.

![img](https://miro.medium.com/max/60/1*Qa4zV-Ys8iXRbPCt2Xt3Zw.png?q=20)

![img]()

Each node can satisfy the heap property with meeting the conditions to be able to apply *min_heapfiy.* This  is because this function iterates the nodes from the bottom (the second  last level) to the top (the root node level). For instance, this  function first applies *min_heapify* to the nodes both of index 4 and index 5 and then applying *min_heapify* to the node of index 2. So the node of the index and its descendent nodes satisfy the heap property when applying *min_heapify.*

Let’s think about the time complexity of *build_min_heap.* First of all, we think the time complexity of *min_heapify*, which is a main part of *build_min_heap.*

*min_heapify* repeats the operation of exchanging the items in an array, which runs in constant time. So the time complexity of *min_heapify* will be in proportional to the number of repeating. In the worst case, *min_heapify* should repeat the operation the height of the tree times. This is because in the worst case, min_heapify will exchange the root nodes with the most depth leaf node. Assuming *h* as the height of the root node, the time complexity of *min_heapify* will take *O*(*h*) time.

The time complexities of *min_heapify* in each depth are shown below. The number of the nodes is also showed in right.

![img](https://miro.medium.com/max/60/1*a-h1jgMmLuIFq_ZhuMmBnw.png?q=20)

![img]()

From the figure, the time complexity of *build_min_heap* will be the sum of the time complexity of inner nodes. The final time complexity becomes:

![img](https://miro.medium.com/max/60/1*nlTVz17IMbUwcrs6SxEWrw.png?q=20)

![img]()

So we should know the height of the tree to get the time complexity.

The sum of the number of nodes in each depth will become *n*. So we will get this equation below.

![img](https://miro.medium.com/max/60/1*OA6ZyHHxwRFMDdspJooQ1A.png?q=20)

![img]()

The equation above stands for the geometric sequence, so we can deform it and get the height of the tree as follow:

![img](https://miro.medium.com/max/60/1*etWYXqoPtFIl5C7j-K_TiA.png?q=20)

![img]()

Finally, we get *O*(*n*) as the time complexity of *build_min_heap*. Also, we get *O*(log*n*) as the time complexity of *min_heapify*.

Here we implement *min_heapify* and *build_min_heap* with Python. the implementation of *min_heapify* will be as follow.

```
def min_heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)
```

First, this method computes the node of the smallest value among the node of index *i* and its child nodes and then exchange the node of the smallest value with the node of index *i*. When the exchange happens, this method applies *min_heapify* to the node exchanged.

Index of a list (an array) in Python starts from 0, the way to access the nodes will change as follow.

- The root node｜*i* = 0
- The parent node｜parent(*i*) = (*i*-1) / 2
- The left child node｜left(*i*) = 2*i* + 1
- The right child node｜right(*i*)=2*i*+2

The variable, *smallest* has the index of the node of the smallest value. If the *smallest* doesn’t equal to the *i*, which means this subtree doesn’t satisfy the heap property, this method exchanges the nodes and executes *min_heapify* to the node of the *smallest*.

The implementation of *build_min_heap* is almost the same as the pseudo-code.

```
def build_min_heap(array):
    for i in reversed(range(len(array)//2)):
        min_heapify(array, i)
```

The  for-loop differs from the pseudo-code, but the behavior is the same.  This for-loop also iterates the nodes from the second last level of  nodes to the root nodes.

Heapsort is one sort algorithm with a heap. It’s really easy to implement it with *min_heapify* and *build_min_heap.* The flow of sort will be as follow. Please note that the order of sort is ascending.

1. Build a heap from an arbitrary array with *build_min_heap.*
2. Swap the first item with the last item in the array.
3. Remove the last item from the array.
4. Run *min_heapify* to the first item.
5. Back to step 2.

In a heap, the smallest item is the first item of an array. The array after step 3 satisfies the conditions to apply *min_heapify* because  we remove the last item after we swap the first item with the last  item. By this nature, we can sort an array by repeating steps 2 to 4.

The implementation of heapsort will become as follow.

```
def heapsort(array):
    array = array.copy()
    build_min_heap(array)    sorted_array = []
    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)    return sorted_array
```

The time complexity of heapsort is *O*(*n*log*n*) because in the worst case, we should repeat *min_heapify* the number of items in array times, which is *n*.

In [the heapq module](https://docs.python.org/3/library/heapq.html)  of Python, it has already implemented some operation for a heap. I  followed the method in MIT’s lecture, the implementation differs from  Python’s. If you’d like to know Python’s detail implementation, please  visit [the source code here](https://github.com/python/cpython/blob/master/Lib/heapq.py). For example, these methods are implemented in Python.

- `heapq.heapify` | corresponds to *build_min_heap*
- `heapq.heapop` | corresponds to swapping items, remove the last item, and *min_heapify* at once*.*

By using those methods above, we can implement heapsort as follow. Please note that it differs from [the implementation of heapsort in the official documents](https://docs.python.org/3/library/heapq.html#basic-examples).

```
import heapqdef heapsort(array):
    h = array.copy()
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(array))]
```

So that’s all for this post. Thank you for reading!

## References

- [MIT OpenCourseWare 4. Heaps and Heap Sort](https://www.youtube.com/watch?v=B7hVxCmfPtM)

​            https://medium.com/policy/9db0094a1e0f?source=post_page-----23d4c78a6962----------------------)