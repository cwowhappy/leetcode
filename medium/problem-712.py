"""
变相的最长公共子序列
"""
class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        minDeleteSumMatrix = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        for (i, a) in enumerate(s1):
            minDeleteSumMatrix[i + 1][0] = minDeleteSumMatrix[i][0] + ord(a)
        for (i, a) in enumerate(s2):
            minDeleteSumMatrix[0][i + 1] = minDeleteSumMatrix[0][i] + ord(a)
        for (i, a) in enumerate(s1):
            for (j, b) in enumerate(s2):
                minDeleteSumMatrix[i + 1][j + 1] = min(minDeleteSumMatrix[i][j + 1] + ord(a), minDeleteSumMatrix[i + 1][j] + ord(b), minDeleteSumMatrix[i][j] + (0 if a == b else (ord(a) + ord(b))))

        return minDeleteSumMatrix[len(s1)][len(s2)]


s1 = "leet"
s2 = "delete"
solution = Solution()
print(solution.minimumDeleteSum(s1, s2))