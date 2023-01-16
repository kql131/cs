# Write a function "longest" that given a string, returns the character repeated 
# the most times **consecutively**, and the length of the longest run. 
# In case of a tie, pick the character appearing first in the input.

# Example:

# print longest("aaaab") == ("a", 4)
# print longest("ab") == ("a", 1)
# print longest("abcabcabc") == ("a", 1)
# print longest("aabb") == ("a", 2)
# print longest("aabbbccccc") == ("c", 5)

import unittest

class LongestConsecutiveString():

    def longest(self, input):

        if (len(input) == 0):
            return (' ', 0)

        if (len(input) == 1):
            return (input[0], 1)

        start = 0
        walker = start
        count = 0
        max = (input[start], 0)

        while (walker < len(input)):
            
            if input[start] == input[walker]:
                count = count + 1
                walker = walker + 1
            else: 
                if count > max[1]:
                    max = (input[start], count)
                count = 0
                start = walker

        if count > max[1]:
            max = (input[start], count)
        
        return max

class Test(unittest.TestCase):

    def setUp(self):
        self.lcs = LongestConsecutiveString()

    def test_normal(self):
        max = self.lcs.longest("aabbbc")
        self.assertEqual(max[0], 'b', "expected to be b")
        self.assertEqual(max[1], 3, "expected to be 3 as max value")

    def test_single_long(self):
        max = self.lcs.longest("bbb")
        self.assertEqual(max[0], 'b', "expected to be b")
        self.assertEqual(max[1], 3, "expected to be 3 as max value")
        
    
    def test_long_tail(self):
        max = self.lcs.longest("abbbcdddd")
        self.assertEqual(max[0], 'd', "expected to be d")
        self.assertEqual(max[1], 4, "expected to be 4 as max value")

    
    def test_single(self):
        max = self.lcs.longest("b")
        self.assertEqual(max[0], 'b', "expected to be b")
        self.assertEqual(max[1], 1, "expected to be 1 as max value")

    
    def test_empty(self):
        max = self.lcs.longest("")
        self.assertEqual(max[0], ' ', "expected to be b")
        self.assertEqual(max[1], 0, "expected to be 0 as max value")

    def test_custom1(self):
        self.assertEqual(self.lcs.longest("aaaab"), ("a", 4))
        self.assertEqual(self.lcs.longest("ab"), ("a", 1))
        self.assertEqual(self.lcs.longest("abcabcabc"), ("a", 1))
        self.assertEqual(self.lcs.longest("aabb"), ("a", 2))
        self.assertEqual(self.lcs.longest("aabbbccccc"), ("c", 5))

if __name__ == '__main__':
    unittest.main()
