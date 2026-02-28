class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        modulo = (10 ** 9) + 7
        concat_bin = ""
        for i in range(1,n+1):
            concat_bin += bin(i)[2:]
        return int(concat_bin,2) % modulo
        

        