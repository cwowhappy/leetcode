class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        longests = [[1, 1] for _ in range(len(nums))]
        for index, num in enumerate(nums):
            for i in range(index):
                if num > nums[i]:
                    length = longests[i][0] + 1
                    if length > longests[index][0]:
                        longests[index][0] = length
                        longests[index][1] = longests[i][1]
                    elif length == longests[index][0]:
                        longests[index][1] += longests[i][1]

        curLongest = 0
        count = 0
        for longest in longests:
            if curLongest < longest[0]:
                curLongest = longest[0]
                count = longest[1]
            elif curLongest == longest[0]:
                count += longest[1]
        return count


nums = [2, 2, 2, 2, 2]
solution = Solution()
print(solution.findNumberOfLIS(nums))