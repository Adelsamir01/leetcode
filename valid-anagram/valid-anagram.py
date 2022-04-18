class Solution(object):
  
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if self.counts(s) == self.counts(t):
            return True
        else:
            return False
        
    def counts(self, x):
        dict = {}
        for i in set(x):
            dict[i] = 0
        for i in x:
            dict[i]+=1
        return dict
        