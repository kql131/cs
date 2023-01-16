import unittest
from typing import List

class BubbleSort:

    def sort(self, arr: List[int]) -> List[int]:
        raise NotImplementedError()

class Test(unittest.TestCase):

    def test(self):
        arr = [4,3,2,1,6,7,8,9,5]
        b = BubbleSort()
        expected = [1,2,3,4,5,6,7,8,9]
        self.assertEquals(expected, b.sort(arr))

if __name__ == '__main__':
    unittest.main()


[4,3,2,1,6,7,8,9,5]


