class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = 0
        for i in range(0, len(words)):
            for j in range(0, len(words[i])):
                if words[i][j] not in allowed:
                    break
            else:
                s += 1    
        return s