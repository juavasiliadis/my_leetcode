class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d_keys = ['type', 'color', 'name']
        d = {}

        for k in d_keys:
            d[k] = []

        for i, j in enumerate(d_keys):
            for k in items:
                d[j].append(k[i])

        s = 0

        for i in d[ruleKey]:
            if i == ruleValue:
                s += 1

        return s