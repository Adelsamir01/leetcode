class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in set(nums):
            dict[i] = 0
        for i in nums:
            dict[i]+=1
        for key,value in dict.items():
            if value == 1:
                return key
            