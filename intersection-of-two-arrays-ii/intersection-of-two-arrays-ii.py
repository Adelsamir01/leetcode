from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2): return self.intersect(nums2,nums1)
        counts = Counter(nums1)
        res = []
        for i in nums2:
            if counts[i] > 0:
                res.append(i)
                counts[i]-=1
        return res