"""
LCS Problem Statement:
Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.

Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""
import unittest

class LongestCommonSubsequence:

    @staticmethod
    def find_lcs(sequence1: str, sequence2: str) -> str:
        pass

class Test(unittest.TestCase):

    def test_easy(self):
        sequence1 = "ABCDGH"
        sequence2 = "AEDFHR"
        expected = "ADH"
        actual = LongestCommonSubsequence.find_lcs(sequence1, sequence2)
        self.assertEqual(actual, expected)