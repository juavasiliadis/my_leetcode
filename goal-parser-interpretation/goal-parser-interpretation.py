class Solution:
    def interpret(self, command: str) -> str:
        s = ''
        for j in range(0, len(command)-1):
            if command[j] == 'G':
                s += 'G'
            if command[j] == '(' and command[j+1] == ')':
                s += 'o'
            if command[j] == '(' and command[j+1] == 'a':
                s += 'al'
        if command[-1] == 'G':
            s += 'G'
        return s