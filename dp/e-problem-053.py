
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        preMaxSum = curMaxSum = nums[0];
        for num in nums[1:]:
            preMaxSum = max(preMaxSum, curMaxSum)
            curMaxSum = max(curMaxSum + num, num)
        return max(preMaxSum, curMaxSum)
