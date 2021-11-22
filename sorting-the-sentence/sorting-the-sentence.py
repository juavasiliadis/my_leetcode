class Solution:
    def sortSentence(self, s: str) -> str:
        d = {}
        s1 = ''
        arr = s.split()
        for i in arr:
            d[i[-1]] = i[:-1]
        items = d.items()
        sorted_items = sorted(items)
        for i in range(0, len(sorted_items)):
            s1 = s1 + sorted_items[i][1] + ' '
        s1 = s1.strip()
        return s1