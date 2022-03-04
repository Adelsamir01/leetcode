class Solution(object):
    def countstrs(self, x):
        count = [0] * 256
        for i in x:
            count[ord(i)]+=1
        return count
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_s = self.countstrs(s)
        count_t = self.countstrs(t)
        
        if count_s == count_t:
            return True
        else:
            return False
            
        