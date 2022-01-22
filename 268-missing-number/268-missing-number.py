class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        l = []
        for i in range(nums[-1]+1):
            print(i)
            if i not in nums:
                l.append(i)
                
        if len(l) == 0:
            return nums[-1]+1
        else:
            return l[0]