class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = 0
        k = 0
        for number in nums:
            while number != 0:
                n += 1
                number = number // 10
            if n % 2 == 0:
                k += 1
            n = 0
        return k