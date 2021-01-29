from heapq import heappush, heappushpop

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lowHeap = [] # max heap
        self.highHeap = [] # min heap
        

    def addNum(self, num: int) -> None:
        if len(self.lowHeap) == len(self.highHeap):
            heappush(self.highHeap, -heappushpop(self.lowHeap, -num))
        else:
            heappush(self.lowHeap, -heappushpop(self.highHeap, num))

    def findMedian(self) -> float:
        if len(self.lowHeap) == len(self.highHeap):
            return float(-self.lowHeap[0] + self.highHeap[0]) / 2.0
        else:
            return float(self.highHeap[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
