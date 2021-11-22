class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        s = 0

        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if mat[i][j] == 1:
                    if mat[i].count(0) == (len(mat[0]) - 1) and ([g[j] for g in mat].count(0) == len(mat) -1):
                        s += 1

        return s