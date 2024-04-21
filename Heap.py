import sys
import Movie
from queue import PriorityQueue


class Heap:
    def __init__(self, m):
        self.max = m
        self.size = 0
        self.heap_arr = [m] * (self.size + 1)

    def getParent(self, child):
        return child // 2

    def getLeftChild(self, index):
        return 2 * index

    def getRightChild(self, index):
        return 1 + (2*index)


    def heapifyDown(self, index):
        l = index * 2 + 1
        r = index * 2 + 2
        biggest = index
        if l < self.size and self.heap_arr[l] > self.heap_arr[biggest]:
            biggest = l
        if r < self.size and self.heap_arr[r] > self.heap_arr[biggest]:
            biggest = r
        if biggest != index:
            temp = self.heap_arr[index]
            self.heap_arr[index] = self.heap_arr[biggest]
            self.heap_arr[biggest] = temp
            index = biggest
            self.heapifyDown(index)

    def extractMax(self):
        # Inspired by Programming Quiz 6
        self.heap_arr[0] = self.heap_arr[--self.size]
        self.heapifyDown(0)

    def kthLargestElements(self, k):
        pq = PriorityQueue()
        for i in range(0, self.size):
            pq.put(self.heap_arr[i])
            if pq.size() < k:
                pq.dequeue()
        return pq.get()
