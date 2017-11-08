class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

    @staticmethod
    def recursive(strings, l, m, n, max_numbers):
        if not max_numbers[l][m][n]:
            max_numbers[l][m][n] = 0

        return max_numbers[l][m][n]
