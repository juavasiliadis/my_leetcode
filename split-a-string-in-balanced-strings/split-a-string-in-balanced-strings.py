class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        r = 0
        sum = 0
        for i in s:
            if i == 'L':
                l += 1
            else:
                r += 1
            if l == r:
                sum += 1
                l = 0
                r = 0
        return sum