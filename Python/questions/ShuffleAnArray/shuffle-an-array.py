class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.current = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.current = self.original[:]
        return self.current
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.current)
        
        for i in range(n):
            newIndex = random.randrange(i, n)
            self.current[i], self.current[newIndex] = self.current[newIndex], self.current[i]
            
        return self.current


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()