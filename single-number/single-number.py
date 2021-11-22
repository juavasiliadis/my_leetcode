class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=list(nums)
        for i in nums:
            if i in n:
                n.remove(i)
                if i in n:
                    n.remove(i)
                else:
                    return i