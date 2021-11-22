class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s = 0
        for i in accounts:
            if sum(i) > s:
                s = sum(i)  
        return s