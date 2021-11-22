class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums = sorted(nums)
        minimum = nums[0]
        maximum = nums[-1]
        import math
        result = math.gcd(minimum, maximum)
        return result