class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        set1 = ''
        set2 = ''

        for i in word1:
            set1 += i
        for i in word2:
            set2 += i

        return (set1 == set2)