from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        #Using Two Pointers L and R
        l = 0 
        result = []
        count = 0
        for r in range(len(s)):
            if s[r] == s[l]:
                count += 1
            else:
                # When two characters are not same, L value becomes R.
                # if count gt 3 , append the result.
                if count >=3:
                    result.append([l,r-1])
                l = r
                count = 1
        if count >= 3:
            result.append([l,r])
        return result
