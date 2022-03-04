class Solution(object):
    def countstrs(self, s):
        count = [0] * 256
        for i in s:
            count[ord(i)]+=1
        return count
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = self.countstrs(s)
        index = -1
        for i in range(len(s)):
            if count[ord(s[i])] == 1:
                index = i
                break
        return index