class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        m_n_of_strings = Solution.count_m_n_of_strings(strs)
        print(m_n_of_strings)
        max_numbers = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        return Solution.recursive1(m_n_of_strings, len(strs) - 1, m, n)

    @staticmethod
    def count_m_n_of_strings(strings):
        m_n_of_strings = []
        for string in strings:
            m_n_of_strings.append(Solution.count_m_n_of_string(string))
        return m_n_of_strings

    @staticmethod
    def count_m_n_of_string(string):
        return [string.count("0"), string.count("1")]

    @staticmethod
    def recursive1(m_n_of_strings, l, m, n):
        if l < 0:
            return 0
        if m >= m_n_of_strings[l][0] and n >= m_n_of_strings[l][1]:
            return max(Solution.recursive1(m_n_of_strings, l - 1, m, n),
                       Solution.recursive1(m_n_of_strings, l - 1, m - m_n_of_strings[l][0], n - m_n_of_strings[l][1]) + 1)
        else:
            return Solution.recursive1(m_n_of_strings, l - 1, m, n)

    @staticmethod
    def recursive(m_n_of_strings, l, m, n, max_numbers):
        if l < 0:
            return 0
        if not max_numbers[m][n]:
            if m >= m_n_of_strings[l][0] and n >= m_n_of_strings[l][1]:
                max_numbers[m][n] = max(Solution.recursive(m_n_of_strings, l - 1, m, n, max_numbers),
                                        Solution.recursive(m_n_of_strings, l - 1, m - m_n_of_strings[l][0],
                                                           n - m_n_of_strings[l][1], max_numbers) + 1)
            else:
                max_numbers[m][n] = Solution.recursive(m_n_of_strings, l - 1, m, n, max_numbers)

        return max_numbers[m][n]


Array = ["1", "0", "1", "0"]
solution = Solution()
print(solution.findMaxForm(Array, 2, 2))
