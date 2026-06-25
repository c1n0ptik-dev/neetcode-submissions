class MaxHeap:
    def __init__(self, arr):
        self.data = []
        self.arr = arr

    def push(self, index):
        self.data.append(index)
        i = len(self.data) - 1
        self.heapify_up(i)
        
    def heapify_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.arr[self.data[parent]] > self.arr[self.data[i]]:
                break
            self.data[i], self.data[parent] = self.data[parent], self.data[i]
            i = parent

    def get_max(self, l, r):
        while self.data[0] < l:
            self.data[0] = self.data.pop()
            self.heapify_down(0)     

        if len(self.data) == 1:
            return self.arr[self.data[0]]
        
        largest = self.data[0]
        return self.arr[largest]

    def heapify_down(self, i):
        largest = i
        l, r = (i * 2) + 1, (i * 2) + 2

        if l < len(self.data) and self.arr[self.data[l]] > self.arr[self.data[largest]]:
            largest = l
        
        if r < len(self.data) and self.arr[self.data[r]] > self.arr[self.data[largest]]:
            largest = r

        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.heapify_down(largest)
        

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = MaxHeap(nums)
        n = len(nums)
        ans = []

        for i in range(k):
            heap.push(i)

        ans.append(heap.get_max(0, k))

        l = 0
        for r in range(k, n):
            heap.push(r)
            l += 1
            ans.append(heap.get_max(l, r))
    
        return ans

                







        