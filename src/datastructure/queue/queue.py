import unittest

class Queue: 

    def __init__(self):
        self.queue = list()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.size() == 0:
            return None
        else:
            return self.queue.pop(0)
    
    def contains(self, data):
        for i in self.queue:
            if self.queue[i] == data:
                return True
        return False

    def print_queue(self):
        if self.size() == 0:
            print("None")
        else:
            for index in reversed(range(0, self.size())):
                print(self.queue[index], end=" ")
    
    def peek(self):
        if self.size() != 0:
            return self.queue[self.size() - 1]
        return None

    def size(self):
        return len(self.queue)
    
class TestQueue(unittest.TestCase):

    def test_enqueue(self):
        queue = Queue()
        nums = [1,2,3,4,5]
        for n in nums: 
            queue.enqueue(n)
        expected = 5
        actual = queue.size()
        self.assertEqual(expected, actual, "queue size should be 5, but got {} instead".format(actual))
        actual = queue.peek()
        self.assertEqual(5, actual, "head of queue should be 5, but got {} instead.".format(actual))

    def test_dequeue(self):
        queue = Queue()
        nums = [1,2,3,4,5]
        for n in nums: 
            queue.enqueue(n)
        actual_head = queue.dequeue()
        self.assertEqual(1, actual_head, "dequeue from head should be 1, but got {} instead.".format(actual_head))
        actual_size = queue.size()
        self.assertEqual(4, actual_size, "dequeue 1 and size should be 4, but got {} instead.".format(actual_size))

    def test_find(self):
        queue = Queue()
        actual = queue.contains(0)
        self.assertEqual(False, actual, "contains() of empty queue should return False, but got {} instead.".format(actual))

        nums = [1,2,3,4,5]
        for n in nums: 
            queue.enqueue(n)
        hasNumber = queue.contains(3) 
        self.assertEqual(True, hasNumber, "contains() should return True because 3 is in the queue, but got {} instead.".format(hasNumber))


if __name__ == "__main__":
    unittest.main(verbosity=3)