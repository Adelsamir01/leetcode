class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums)==1:
            return nums
        z = 0
        nz = 1
        while z < nz and nz<len(nums):
            if nums[z] == 0 and nums[nz] != 0:
                nums[z] = nums[nz]
                nums[nz] = 0
                z+=1
                nz+=1
            elif nums[z] == 0 and nums[nz] == 0:
                nz+=1
            else:
                z+=1
                nz+=1
        return nums