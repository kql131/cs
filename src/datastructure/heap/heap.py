import unittest
import math

class MinHeap:
    
    def __init__(self):
        self.heap = [None]
    
    def get_parent(self, index) -> int:
        """
        Should return the index of parent. 
        """
        return math.floor(index/2)
    
    def get_left(self, index) -> int:
        return index * 2
    
    def get_right(self, index) -> int:
        return (index * 2) + 1
    
    def insert(self, value):
        pass 
    
    def delete_root(self, value):
        pass 
    
    def heapify(self):
        pass 
    
class TestMinHeap(unittest.TestCase):
    
    def test_get_parent(self):
        arr = [None, 3, 6, 8, 2, 4]
        my_heap = MinHeap()
        my_heap.heap = arr
        self.assertEqual(1, my_heap.get_parent(3), "should return parent")
        self.assertEqual(1, my_heap.get_parent(2), "should return parent")
        self.assertEqual(2, my_heap.get_parent(4), "should return parent")
        self.assertEqual(2, my_heap.get_parent(5), "should return parent")

    def test_get_left(self):
        arr = [None, 3, 6, 8, 2, 4]
        my_heap = MinHeap()
        my_heap.heap = arr
        self.assertEqual(2, my_heap.get_left(1), "should return left")
        self.assertEqual(4, my_heap.get_left(2), "should return left")

    def test_get_right(self):
        arr = [None, 3, 6, 8, 2, 4]
        my_heap = MinHeap()
        my_heap.heap = arr
        self.assertEqual(3, my_heap.get_right(1), "should return right")
        self.assertEqual(5, my_heap.get_right(2), "should return right")
        
if __name__ == "__main__":
    unittest.main()