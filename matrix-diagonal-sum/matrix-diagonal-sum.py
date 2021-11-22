class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        j = len(mat)-1
        for i in range(0, len(mat)):
            sum += mat[i][i] + mat[i][j]
            j = j - 1

        if len(mat) % 2 != 0:
            sum = sum - mat[(len(mat)-1) // 2][(len(mat)-1) // 2]
        return sum