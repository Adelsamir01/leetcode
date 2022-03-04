class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        j = len(s)-1
        i = 0
        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i+=1
            j-=1
            
        return s