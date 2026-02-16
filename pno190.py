class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32): # 32 bit integer
            result = result << 1 # This is what reverses the integer(bits)
            remainder = n % 2
            result += remainder # Add this remainder (1 or 0) to the result
            n = n >> 1
        return result