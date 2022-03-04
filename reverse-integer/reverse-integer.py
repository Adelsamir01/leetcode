class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        flag = False
        if x < 0:
            flag = True
            x= 0-x
            
        result = 0
        while x > 0:
            mod = x % 10
            x = x / 10
            result = result * 10 + mod
            
        if flag:
            result = 0-result
        if result >= -2**31 and result <= 2**31:
            return result
        else:
            return 0