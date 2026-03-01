class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1 
        if len(nums) == 1:
            return nums[0]
        while l <= r:
            m = l + ( r - l)//2
            if m == 0:
                if nums[m] != nums[m + 1]:
                    return nums[m]
                else:
                    l = m + 1
            
            if m == len(nums) - 1:
                if nums[m] != nums[m - 1]:
                    return nums[m]
                else:
                    r = m - 1

            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            elif nums[m] == nums[m-1]:
                if m % 2 == 0:
                    r = m -1
                else:
                    l = m + 1
            elif nums[m] == nums[m+1]:
                if m % 2 == 0:
                    l = m + 1
                else:
                    r = m - 1

            
        


