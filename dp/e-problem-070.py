"""
解题思路：

"""
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        num1 = 1
        num2 = 0
        for i in range(1, n):
            tmp = num1
            num1 = num1 + num2
            num2 = tmp

        return num1 + num2
