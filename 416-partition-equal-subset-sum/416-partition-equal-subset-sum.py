class Solution(object):
    def canPartition(self, nums):
        if sum(nums)%2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums)//2
        
        for i in range(len(nums)):
            newdp = set()
            for j in dp:
                if (j+nums[i]==target):
                    return True
                newdp.add(j+nums[i])
                newdp.add(j)
            dp = newdp
        return True if target in dp else False