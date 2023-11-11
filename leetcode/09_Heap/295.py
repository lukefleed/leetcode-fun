import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeap = [] 
        self.minHeap = []
        # I am using a maxHeap to store the smaller half of the numbers and a minHeap to store the larger half of the numbers. 
        # This gives me direct access to the one or two middle values (they're the tops of the heaps), so getting the median takes O(1) time. 
        # And adding a number takes O(log n) time.

    def addNum(self, num: int) -> None:
            
            if len(self.maxHeap) == 0: # if maxHeap is empty then add the number to maxHeap
                heapq.heappush(self.maxHeap, -num)
                return
    
            if num <= -self.maxHeap[0]: # if the number is less than the top of maxHeap then add it to maxHeap, it means it is in the smaller half
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num) # else add it to minHeap, it means it is in the larger half
    
            if len(self.maxHeap) > len(self.minHeap) + 1: # if the size of maxHeap is greater than the size of minHeap by more than 1, then we need to balance the heaps
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            elif len(self.maxHeap) < len(self.minHeap): # if the size of minHeap is greater than the size of maxHeap, then we need to balance the heaps
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap)) 
        

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            return -self.maxHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
