class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        longest = [1 for _ in range(len(nums))]
        for index, num in enumerate(nums):
            for i in range(index):
                if num > nums[i]:
                    length = longest[i] + 1
                    if length > longest[index]:
                        longest[index] = length
        return max(longest)


nums = []
solution = Solution()
print(solution.lengthOfLIS(nums))