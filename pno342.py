class Solution:
    def isPowerOfFour(self, n: int) -> bool:  
        count_zero = bin(n).split('b')[1].count('0')
        if n == 0:
            return False   
        if count_zero % 2 == 1:
            return False
        if n & n-1 == 0:
            return True
        else:
            return False