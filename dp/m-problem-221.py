
class Solution:
    def maximalSquare(self, matrix):
        height = len(matrix)
        if 0 == height:
            return 0
        width = len(matrix[0])
        maxLen = 0
        diagonalMaxLen = 0
        currentMaxLens = [0 for _ in range(0, width + 1)]
        for h in range(0, height):
            for w in range(0, width):
                nextDiagonalMaxLen = currentMaxLens[w + 1]
                if matrix[h][w] == '1':
                    currentMaxLens[w + 1] = min(diagonalMaxLen, currentMaxLens[w], currentMaxLens[w + 1]) + 1
                else:
                    currentMaxLens[w + 1] = 0
                diagonalMaxLen = nextDiagonalMaxLen
                maxLen = max(maxLen, currentMaxLens[w + 1])
        return maxLen ** 2


matrix = [["1","0","1","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["1","1","0","1","1"],["0","1","1","1","1"]]
for i in range(len(matrix)):
    print(matrix[i])
solution = Solution()
print(solution.maximalSquare(matrix))