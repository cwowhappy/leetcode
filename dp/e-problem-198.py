class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        sum1 = 0
        sum2 = nums[0]
        for num in nums[1:]:
            tmp = sum1
            sum1 = max(sum1, sum2)
            sum2 = max(tmp + num, num)
        return max(sum1, sum2)