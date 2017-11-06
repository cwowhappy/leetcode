class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.lenNums = len(nums)
        self.sums = [0 for i in range(self.lenNums + 1)]
        index = 1
        for num in nums:
            self.sums[index] = self.sums[index - 1] + num
            index += 1

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j + 1] - self.sums[i]


nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)
print(numArray.sumRange(0, 2))
print(numArray.sumRange(2, 5))
print(numArray.sumRange(0, 5))
