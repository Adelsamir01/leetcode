class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        fact = 1
        for i in range(1,n+1):
            fact = fact * i
        fact = str(fact)
        count = 0
        for i in range(len(fact)-1,-1,-1):
            if fact[i] == '0':
                count+=1
            else:
                return count
            