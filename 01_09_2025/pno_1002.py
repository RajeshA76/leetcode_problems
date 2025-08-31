
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        char_dict = {}
        for char in words[0]:
            if char_dict.get(char):
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        for word in words[1:]:
            temp_dict = {}
            for char in word:
                if temp_dict.get(char):
                    temp_dict[char] += 1
                else:
                    temp_dict[char] = 1
            for c in list(char_dict.keys()):
                if c in temp_dict:
                    char_dict[c] = min(temp_dict[c],char_dict[c])
                else:
                    del char_dict[c]
        result = []
        for char, freq in char_dict.items():
            result.extend([char] * freq)
        return result


        