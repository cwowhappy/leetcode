class Solution:

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        index_begin = 0
        index_end = len_nums - 1
        while index_begin < index_end:
            index_mid = index_begin + (index_end - index_begin) // 2
            if nums[index_begin] <= nums[index_mid] <= nums[index_end]:
                break
            else:
                if nums[index_begin] > nums[index_mid]:
                    index_end = index_mid
                if nums[index_end] < nums[index_mid]:
                    index_begin = index_mid + 1
        return nums[index_begin]


nums = [3, 1, 2]
solution = Solution()
print(solution.findMin(nums))