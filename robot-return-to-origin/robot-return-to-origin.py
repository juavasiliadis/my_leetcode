class Solution:
    def judgeCircle(self, moves: str) -> bool:
        i = 0
        j = 0
        for k in moves:
            if k == 'L':
                i = i - 1
            if k == 'R':
                i = i + 1
            if k == 'D':
                j = j - 1
            if k == 'U':
                j = j + 1
        return (i == 0 and j == 0)