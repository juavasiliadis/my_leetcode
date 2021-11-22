class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        s = set(arr)
        for i in s:
            d[i] = arr.count(i)
        return len(set(d.values())) == len(d.keys())