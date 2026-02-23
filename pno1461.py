class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        substr = set()
        l = 0
        for r in range(1,len(s)+1):
            if r >= k:
                if s[l:r] not in substr:
                    substr.add(s[l:r])
                l += 1
        return len(substr) == 2**k
