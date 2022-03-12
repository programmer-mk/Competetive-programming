import copy

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix[0])
        n = len(matrix)
        change_matrix = copy.deepcopy(matrix)

        for i in range(n):
            for j in range(m):
                if not matrix[i][j] and not change_matrix[i][j]:
                    matrix[i] = [0] * m
                    for row in matrix:
                        row[j] = 0

        return matrix