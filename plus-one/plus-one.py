class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        j = 0
        num = 0
        for i in range(len(digits)-1,-1,-1):
            num += digits[i]*(10**j)
            j+=1
        num = str(num+1)
        l = []
        for i in range(len(num)):
            l.append(int(num[i]))
        return l