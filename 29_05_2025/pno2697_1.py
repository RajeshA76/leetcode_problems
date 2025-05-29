class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        lp,rp = 0, len(s) -1
        res_array = [None] * len(s)
        while lp <= rp:
            if s[lp] != s[rp]:
                if ord(s[lp]) < ord(s[rp]):
                    res_array[lp] = res_array[rp] = s[lp]
                else:
                    res_array[lp] = res_array[rp] = s[rp]
            else:
                res_array[lp] = res_array[rp] = s[lp]
            lp,rp = lp + 1, rp -1
        return "".join(res_array)
