class Solution:

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        index_begin = 0
        index_end = len_nums - 1
        if index_begin < index_end:
            return self.findMinRecursive(nums, index_begin, index_end)
        else:
            return nums[index_begin]

    def findMinRecursive(self, nums, index_begin, index_end):
        if index_begin == index_end:
            return nums[index_begin]
        if index_begin + 1 == index_end:
            return nums[index_begin] if nums[index_begin] < nums[index_end] else nums[index_end]
        else:
            index_mid = index_begin + (index_end - index_begin) // 2
            if nums[index_begin] == nums[index_mid] == nums[index_end]:
                minimum = self.findMinRecursive(nums, index_begin, index_mid)
                if minimum == nums[index_mid]:
                    minimum = self.findMinRecursive(nums, index_mid, index_end)
                return minimum
            else:
                if nums[index_begin] < nums[index_mid] <= nums[index_end] or nums[index_begin] <= nums[index_mid] < nums[index_end]:
                    return nums[index_begin]
                else:
                    if nums[index_begin] > nums[index_mid]:
                        return self.findMinRecursive(nums, index_begin, index_mid)
                    if nums[index_end] < nums[index_mid]:
                        return self.findMinRecursive(nums, index_mid + 1, index_end)


nums = [3, 3, 3, 1, 2, 3]
solution = Solution()
print(solution.findMin(nums))
