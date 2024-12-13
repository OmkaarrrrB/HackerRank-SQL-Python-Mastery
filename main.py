#Leetcode75

"""
Question Link
https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

Question no:1768
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
"""
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word3 = ""
        for i, j in zip(word1, word2):
            word3 += i + j
        word3 += word1[len(word2):] + word2[len(word1):]
        return word3

