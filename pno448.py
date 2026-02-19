from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashset = set(nums)
        result = []
        for i in range(1,len(nums)+1):
            if i not in hashset:
                result.append(i)
        return result