class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        
    # write your code in Python
        result = {}
        for number in arr:
            result[number] = result.get(number-difference, 0) + 1
        return max(result.values())
    