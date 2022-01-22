class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # base case
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        
        l = []
        for i in range(len(nums)):
            m = nums[i]
            remLst = nums[:i] + nums[i+1:]
            
            for p in self.permute(remLst):
                l.append([m] + p)
        return l
            
            
                
                
        