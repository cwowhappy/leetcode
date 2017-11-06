class Solution:
    def findLength(self, A, B):
        """
        :param A:
        :param B:
        :return:
        """
        curMaxLength = 0
        lengthMatrix = [[0 for i in range(len(A) + 1)] for j in range(len(B) + 1)]
        for (i, a) in enumerate(A):
            for (j, b) in enumerate(B):
                if a == b:
                    lengthMatrix[i + 1][j + 1] = lengthMatrix[i][j] + 1
                else:
                    lengthMatrix[i + 1][j + 1] = 0
                if curMaxLength < lengthMatrix[i + 1][j + 1]:
                    curMaxLength = lengthMatrix[i + 1][j + 1]

        return curMaxLength


A = [1, 2, 3, 2, 1]
B = [3, 2, 1, 4, 7]

solution = Solution()
print(solution.findLength(A, B))
