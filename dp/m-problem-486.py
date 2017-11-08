"""
注意求解目标：Player1 能否赢 Player2，并不在意Player1 和 Player2实际得的分数
这样就可以把问题抽象成：
针对给定数列，Player1 比 Player2 最多能多获取多少分
"""

class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        score_diff = [[None for _ in range(0, len(nums))] for _ in range(0, len(nums))]
        return Solution.recursive(nums, 0, len(nums) - 1, score_diff) >= 0

    @staticmethod
    def recursive(numbers, start, end, score_diff):
        if not score_diff[start][end]:
            score_diff[start][end] = max(numbers[start] - Solution.recursive(numbers, start + 1, end, score_diff),
                                         numbers[end] - Solution.recursive(numbers, start, end - 1,
                                                                           score_diff)) if start < end else numbers[start]
        return score_diff[start][end]


nums = [1, 15, 3]
solution = Solution()
print(solution.PredictTheWinner(nums))
