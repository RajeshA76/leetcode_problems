class Solution(object):

    def helper(self,l,r,arr):
        while l < r:
            arr[l],arr[r] = arr[r],arr[l]
            l += 1
            r -= 1
        return arr

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.helper(0,len(nums)-1,nums)
        self.helper(0,k-1,nums)
        self.helper(k,len(nums)-1,nums)
        return nums


        



        