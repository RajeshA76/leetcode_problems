import random
class RandomizedSet(object):

    def __init__(self):
        self.hashmap = {}
        self.array = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.hashmap:
            self.hashmap[val] = len(self.array)
            self.array.append(val)
            return True
        else:
            return False
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hashmap:
            last_val = self.array[-1]
            self.array[self.hashmap[val]] = last_val
            self.hashmap[last_val] = self.hashmap[val]
            del self.hashmap[val]
            self.array.pop()
            return True
        else:
            return False


    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()