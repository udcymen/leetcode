class FreqStack:

    def __init__(self):
        self.frequency = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxFrequncey = 0

    def push(self, x: int) -> None:
        occur = self.frequency[x] + 1
        self.frequency[x] = occur
        self.group[occur].append(x)
        
        if occur > self.maxFrequncey:
            self.maxFrequncey = occur

    def pop(self) -> int:
        result = self.group[self.maxFrequncey].pop()
        self.frequency[result] -= 1
        
        if len(self.group[self.maxFrequncey]) == 0:
            self.maxFrequncey -= 1
            
        return result
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()