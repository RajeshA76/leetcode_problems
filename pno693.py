class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = None
        for bit in bin(n):
            if prev == None or bit != prev:
                prev = bit
            else:
                return False
        return True