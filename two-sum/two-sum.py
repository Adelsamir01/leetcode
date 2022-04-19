class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        slow = 0
        fast = 1
        while fast>slow:
            if nums[slow]+nums[fast] == target:
                return [slow, fast]
            elif fast<len(nums)-1:
                fast+=1
            else:
                slow+=1
                fast=slow+1