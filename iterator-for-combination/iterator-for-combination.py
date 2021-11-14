class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.len = len(characters)
        self.characters = characters
        self.pointers = [i for i in range(combinationLength)]
        self.pointers[-1] -= 1
        self.thres = [i for i in range(self.len -len(self.pointers), self.len)]

    def next(self):
        """
        :rtype: str
        """
        idx = 1
        while self.pointers[-idx] + idx >= self.len:
            idx += 1
        self.pointers[-idx] += 1
        idx -= 1
        while idx!=0:
            self.pointers[-idx] = self.pointers[-idx-1]+1
            idx -= 1
            
        ans = ""
        for p in self.pointers:
            ans += self.characters[p]
        return ans
    
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pointers != self.thres    


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
