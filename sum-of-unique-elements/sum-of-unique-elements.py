class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        l1 = []
        repeat = []
        result = 0
        for i in nums:
            if i not in l1:
                l1.append(i)
            else:
                repeat.append(i)
        nums_c = nums.copy()
        for i in nums:
            if i in repeat:
                nums_c.remove(i)
        result = sum(nums_c)
        return result