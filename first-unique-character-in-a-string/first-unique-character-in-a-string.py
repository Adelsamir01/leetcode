class Solution(object):
    
    def firstUniqChar(self, s):
        
        ss = list(set(s))
        dict = {}
        for i in ss:
            dict[i] = 0
        for i in s:
            dict[i] += 1
        print (dict)
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        return -1