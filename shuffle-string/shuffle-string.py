class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {}
        l = ''
        for i in range(0, len(s)):
            d[indices[i]] = s[i]
        items = d.items()
        sorted_items = sorted(items)
        for i in range(0, len(s)):
            l = l + sorted_items[i][1]
        return l