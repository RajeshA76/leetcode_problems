class Solution:
    def findComplement(self, num: int) -> int:
        stack = []
        while num>0:
            stack.append(int(not(num % 2)))
            num //= 2
        result = "".join(str(i) for i in stack[::-1])
        return int(result,2)