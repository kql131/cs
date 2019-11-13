import unittest


class MinHeap:
    def __init__(self):
        self.data = [None]
        self.count = 0

    def min_heapify(self, index) -> None:
        if self.count < 2:
            return None

        while index > 1:
            parent = self.data[index // 2]
            child = self.data[index]

            if parent < child:
                return None

            self.data[index // 2], self.data[index] = self.data[index], self.data[index // 2]
            index = index // 2
        return None

    def insert(self, val):
        self.data.append(val)
        self.count += 1
        return self.min_heapify(self.count)

    def remove(self) -> None:
        # swap first elem with the last and pop last elem
        self.data[1], self.data[-1] = self.data[-1], self.data[1]
        self.count -= 1
        top = self.data.pop()

        # re-heapify after removing the top element
        index = 1
        parent = self.data[index]

        if self.count <= 2:
            if self.count == 2:
            # case1: count: 2, only a left child and root; compare and swap if necessary
                left_child = self.data[2 * index]
                if parent > left_child:
                    self.data[index], self.data[2 * index] = self.data[2 * index], self.data[index]
            # case2: count: 1, no children or no root
            return top

        # case3: count > 2: 2 children
        while index < self.count:
            parent = self.data[index]
            left = self.data[2 * index] if 2 * index <= self.count else float('inf')
            right = self.data[(2 * index) + 1] if (2 * index) + 1 <= self.count else float('inf')

            if parent < left and parent < right:
                return top

            if parent > left and parent > right:
                # determine which child is smaller
                if left < right:
                    self.data[index], self.data[2 * index] = self.data[2 * index], self.data[index]
                    index *= 2
                else:
                    # right > left
                    self.data[index], self.data[(2 * index) + 1] = self.data[(2 * index) + 1], self.data[index]
                    index = (2 * index) + 1
            elif parent > left and right == float('inf'):
                self.data[index], self.data[2 *index] = self.data[2 * index], self.data[index]
                index *= 2
            else:
                # parent < left but parent > right
                self.data[index], self.data[(2 * index) + 1] = self.data[(2 * index) + 1], self.data[index]
                index = (2 * index) + 1
        return top

    def peek(self) -> int or None:
        if self.count < 1:
            print('There are no items in the heap.')
            return None
        print('peek value: ', self.data[1])
        return self.data[1]

    def get_parent_of_val(self, val: int) -> int or None:
        if val not in self.data:
            return None

        for i, d in enumerate(self.data):
            if d == val:
                return self.data[i // 2]

    def get_left_child_of_val(self, val: int) -> int or None:
        if val not in self.data:
            return None

        for i, d in enumerate(self.data):
            if d == val:
                if 2 * i <= self.count:
                    return self.data[2 * i]
                else:
                    return None

    def get_right_child_of_val(self, val: int) -> int or None:
        if val not in self.data:
            return None

        for i, d in enumerate(self.data):
            if d == val:
                if (2 * i) + 1 <= self.count:
                    return self.data[(2 * i) + 1]
                else:
                    return None

    def get_children_of_val(self, val: int) -> list or None:
        if val not in self.data:
            return None

        left = self.get_left_child_of_val(val)
        right = self.get_right_child_of_val(val)
        return [left, right]


class TestMinHeap(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_peek_not_empty(self):
        heap = MinHeap()
        data = [9,2,3,8,6,1,5,7]
        for d in data:
            heap.insert(d)

        actual = heap.peek()
        expected = 1
        self.assertEqual(actual, expected, 'peek should return the top value: 1')

    def test_peek_empty(self):
        heap = MinHeap()
        actual = heap.peek()
        expected = None
        self.assertEqual(actual, expected, 'peek should return None')

    def test_insert(self):
        heap = MinHeap()
        data = [9,2,3,8,6,1,5,7]
        for d in data:
            heap.insert(d)

        actual = heap.data[1:]
        expected = [1, 6, 2, 7, 8, 3, 5, 9]
        self.assertEqual(actual, expected, 'data should be min heapified')

    def test_remove(self):
        heap = MinHeap()
        data = [9,2,3,8,6,1,5,7]
        for d in data:
            heap.insert(d)

        print('before remove: ',heap.data[1:])
        actual = heap.remove()
        expected = 1
        print('after remove: ',heap.data[1:])
        self.assertEqual(actual, expected, 'the top element, 1, should be removed')

    def test_get_parent_val(self):
        heap = MinHeap()
        data = [9, 2, 3, 8, 6, 1, 5, 7]
        for d in data:
            heap.insert(d)

        actual = heap.get_parent_of_val(8)
        expected = 6
        self.assertEqual(actual, expected, 'the parent of 8 should be 6.')

    def test_get_left_child_of_val(self):
        heap = MinHeap()
        data = [9, 2, 3, 8, 6, 1, 5, 7]
        for d in data:
            heap.insert(d)

        actual = heap.get_left_child_of_val(6)
        expected = 7
        self.assertEqual(actual, expected, 'the left child of 6 should be 7.')

    def test_get_invalid_left_child(self):
        heap = MinHeap()
        data = [9, 2, 3, 8, 6, 1, 5, 7]
        for d in data:
            heap.insert(d)

        actual = heap.get_left_child_of_val(9)
        expected = None
        self.assertEqual(actual, expected, 'the left child of 9 should be None.')

    def test_get_right_child_of_val(self):
        heap = MinHeap()
        data = [9, 2, 3, 8, 6, 1, 5, 7]
        for d in data:
            heap.insert(d)

        actual = heap.get_right_child_of_val(6)
        expected = 8
        self.assertEqual(actual, expected, 'the right child of 6 should be 8.')

    def test_get_children_of_val(self):
        heap = MinHeap()
        data = [9, 2, 3, 8, 6, 1, 5, 7]
        for d in data:
            heap.insert(d)

        actual = heap.get_children_of_val(2)
        expected = [3, 5]
        self.assertEqual(actual, expected, 'the children of 6 should be [3, 5].')
