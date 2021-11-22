class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l = 0
        result = ''
        new_word = list(word)
        for i in range(len(word)):
            if word[i] == ch:
                l = i + 1
                break

        new_word[:l] = new_word[:l][::-1]
        for i in new_word:
            result += i
        return result