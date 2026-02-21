class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        result = 0
        primes = {2,3,5,7,11,13,17,19}
        for num in range(left,right+1):
            number = bin(num).count('1')
            if number in primes:
                result +=1
        return result
