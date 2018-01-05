class Solution:
    def search(self, nums, target):
        len_nums = len(nums)
        if 0 == len_nums:
            return -1
        else:
            index = -1
            index_begin = 0
            index_end = len_nums - 1
            while index_begin <= index_end:
                index_mid = index_begin + (index_end - index_begin) // 2
                print(index_mid)
                if target == nums[index_begin]:
                    index = index_begin
                    break
                elif target == nums[index_mid]:
                    index = index_mid
                    break
                elif target == nums[index_end]:
                    index = index_end
                    break
                elif (nums[index_begin] < target < nums[index_mid]) or (nums[index_begin] > nums[index_mid] and (nums[index_begin] < target or target < nums[index_mid])):
                    index_end = index_mid - 1
                elif (nums[index_mid] < target < nums[index_end]) or (nums[index_end] < nums[index_mid] and (nums[index_begin] < target or target < nums[index_mid])):
                    index_begin = index_mid + 1
                else:
                    break
            return index


solution = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
print(solution.search(nums, 0))