class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        sum = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    sum += 1
        sum = int(sum /2)
        return sum