class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        result = ''
        s = s.split()

        for i in s[0:k]:
            result = result + i + ' '
        result = result.strip()
        return result