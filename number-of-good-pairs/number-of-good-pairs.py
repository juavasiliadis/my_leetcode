class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = 0
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] == nums[j]:
                    n = n + 1
        return n