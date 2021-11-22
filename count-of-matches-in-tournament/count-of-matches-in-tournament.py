class Solution:
    def numberOfMatches(self, n: int) -> int:
        s = 0
        while n != 1:
            m = n // 2
            n = n - m
            s += m
        return s