class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = 0
        result = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if j != i and nums[j] < nums[i]:
                    n = n+1
            result.append(n)
            n = 0
        return result