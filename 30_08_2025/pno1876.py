class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result = 0
        for index in range(len(s)-2):
            if len(s[index:index+3]) == len(set(s[index:index+3])):
                result += 1
        return result

