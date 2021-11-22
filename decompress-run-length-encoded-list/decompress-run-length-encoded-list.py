class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            if i % 2 == 0:
                result = result + [nums[i+1]]*nums[i]
        return result