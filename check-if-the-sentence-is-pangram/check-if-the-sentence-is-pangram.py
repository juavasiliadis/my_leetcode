class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        import string
        s = string.ascii_lowercase
        unique_sentence = set(sentence)
        return len(unique_sentence) == len(s)