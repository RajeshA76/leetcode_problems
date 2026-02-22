class Solution:
    def binaryGap(self, n: int) -> int:
        binary_n = bin(n)
        if binary_n.count('1') <=1 :
            return 0
        prev = False
        result = 0
        for index in range(len(binary_n)):
            if binary_n[index] == '1':
                if prev:
                    result = max(result,index-prev)
                prev = index
        return result
            
            