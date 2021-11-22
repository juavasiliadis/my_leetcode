class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''

        for i in range(min(len(word1), len(word2))):
            result = result + word1[i]
            result = result + word2[i]

        if len(word1) != 1 and len(word2) != 1:
            if len(word2) > len(word1):
                result = result + word2[len(word1):]
            if len(word1) > len(word2):
                result = result + word1[len(word2):]

        if len(word1) != 1 and len(word2) == 1:
            result = result + word1[1:]

        if len(word2) != 1 and len(word1) == 1:
            result = result + word2[1:]

        if len(word1) == len(word2) == 1:
            result = result
        return result