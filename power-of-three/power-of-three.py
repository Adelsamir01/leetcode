class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 2:
            return False
        i = 1
        while i <= n:
            if i == n:
                return True
            else:
                i*=3
        return False