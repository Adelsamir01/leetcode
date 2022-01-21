class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        u = len(nums)-1
        
        while u >= l:
            mid = (l+u) // 2
            
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    u = mid - 1
        return -1