# this is teh solution to the problem of leetcode :- 329. Longest Increasing Path in a Matrix
# i hope you like this

class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            if memo[row][col] != -1:
                return memo[row][col]

            max_path = 1
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if 0 <= newRow < m and 0 <= newCol < n and matrix[newRow][newCol] > matrix[row][col]:
                    length = 1 + dfs(newRow, newCol)
                    max_path = max(max_path, length)

            memo[row][col] = max_path
            return max_path

        longest_path = 0
        memo = [[-1] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                longest_path = max(longest_path, dfs(i, j))

        return longest_path
