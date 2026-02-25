class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        count_dict = {}
        for num in arr:
            count = bin(num).count('1')
            if count not in count_dict:
                count_dict[count] = [num]
            else:
                count_dict[count].append(num)
        result = []
        for key in count_dict:
            result.extend(sorted(count_dict[key]))
        return result
        