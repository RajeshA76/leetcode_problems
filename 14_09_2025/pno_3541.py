class Solution:
    def maxFreqSum(self, s: str) -> int:
        string_list = [0]* 26
        vowels = ['a','e','i','o','u']
        max_vowel = 0
        max_consonant = 0
        for char in s:
            string_list[ord(char)- ord('a')] += 1
        for index,value in enumerate(string_list):
            if chr(ord('a') + index) in vowels:
                if value > max_vowel:
                    max_vowel = value
            else:
                if value > max_consonant:
                    max_consonant = value
        return max_vowel + max_consonant


        
            
