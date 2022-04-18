import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleanS = self.cleanS(s)
        if len(cleanS) == 0:
            return True
        right = len(cleanS)-1
        left = 0
        while right > left:
            if cleanS[right] != cleanS[left]:
                return False
            left+=1
            right-=1
            
        return True
    def cleanS(self, s):
        az_nums = list(string.ascii_lowercase) + [str(i) for i in range(10)]
        l = []
        for i in s.lower():
            if i in az_nums:
                l.append(i)
        return l