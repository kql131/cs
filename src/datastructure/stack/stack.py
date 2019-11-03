import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self, size):
        self.data = None
        self.size = size
        self.count = 0
        self.head = None

    def push(self, val) -> bool:
        # return False if the new item overflows the stack
        if self.count + 1 > self.size:
            return False

        node = Node(val)
        if self.data is None:
            self.data = node
            self.head = node
            self.count += 1
        else:
            node.next = self.head
            self.head = node
            self.count += 1

        return True

    def pop(self):
        # catch when stack is empty
        if self.count - 1 <= 0:
            return False

        popped = self.head.val
        # move head back
        self.head = self.head.next
        self.count -= 1

        return popped

    def peek(self):
        # return False when stack is empty
        if self.count == 0:
            return False

        return self.head.val

    def is_empty(self) -> bool:
        if self.data is None or self.count == 0:
            return True

        return False



class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        pass


    def test_stack_size(self):
        stack = Stack(1)
        stack.push(5)

        actual = stack.push(3)
        expected = False
        self.assertEqual(actual, expected, 'should return False because stack is full')


    def test_push(self):
        stack = Stack(5)

        actual = stack.push(3)
        expected = True

        actual_count = stack.count
        expected_count = 1
        self.assertEqual(actual, expected, 'should return True when added succesfully')
        self.assertEqual(actual_count, expected_count, 'should return 1 after 1 val has been added')


    def test_pop(self):
        stack = Stack(5)

        stack.push(1)
        stack.push(2)
        stack.push(3)

        actual = stack.pop()
        expected = 3

        actual_count = stack.count
        expected_count = 2

        self.assertEqual(actual, expected, 'should return the popped value, 3')
        self.assertEqual(actual_count, expected_count, 'should return 2 total items remaining')


    def test_peek(self):
        stack = Stack(5)

        stack.push(1)
        stack.push(2)
        stack.push(3)

        actual = stack.peek()
        expected = 3

        self.assertEqual(actual, expected, 'should return the top value, 3')


    def test_peek_when_stack_is_empty(self):
        stack = Stack(3)

        actual = stack.peek()
        expected = False

        self.assertEqual(actual, expected, 'should return False because stack contains no items')


    def test_is_empty_true(self):
        stack = Stack(3)

        actual = stack.is_empty()
        expected = True

        self.assertEqual(actual, expected, 'should return True because stack contains no items')


    def test_is_empty_false(self):
        stack = Stack(3)
        stack.push(2)
        stack.push(1)

        actual = stack.is_empty()
        expected = False

        self.assertEqual(actual, expected, 'should return False because stack contains items')

