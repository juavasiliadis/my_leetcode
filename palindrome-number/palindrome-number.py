class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        count = 0
        if len(a) % 2 == 0:
            if len(a) != 2:
                for i in range(0, len(a) // 2):
                    if a[i] == a[-(i + 1)]:
                        count += 1
            else:
                if a[0] == a[-1]:
                    count = 1
        else:
            for i in range(0, len(a) // 2):
                if a[i] == a[-(i+1)]:
                    count += 1

        return count == len(a) // 2
