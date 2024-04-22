import sys
import Movie
from queue import PriorityQueue


class Heap:
    def __init__(self):
        self.max = -1
        self.size = 0
        self.heap_arr = []

    def getArr(self):
        return self.heap_arr

    def heapifyDown(self, index, idealMovie):
        l = index * 2 + 1
        r = index * 2 + 2
        biggest = index
        if l < self.size and self.heap_arr[l].getSimilarity(idealMovie) > self.heap_arr[biggest].getSimilarity(idealMovie):
            biggest = l
        if r < self.size and self.heap_arr[r].getSimilarity(idealMovie) > self.heap_arr[biggest].getSimilarity(idealMovie):
            biggest = r
        if biggest != index:
            temp = self.heap_arr[index]
            self.heap_arr[index] = self.heap_arr[biggest]
            self.heap_arr[biggest] = temp
            index = biggest
            self.heapifyDown(index, idealMovie)

    def heapifyUp(self, index, idealMovie):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap_arr[parent_index].getSimilarity(idealMovie) < self.heap_arr[index].getSimilarity(idealMovie):
                self.heap_arr[parent_index], self.heap_arr[index] = self.heap_arr[index], self.heap_arr[parent_index]
                index = parent_index
            else:
                break

    def extractMax(self, idealMovie):
        # Inspired by Programming Quiz 6
        if self.size == 0:
            return None
        if self.size == 1:
            self.size -= 1
            return self.arr.pop()
        temp = self.heap_arr[0]
        self.heap_arr[0] = self.heap_arr[self.size-1]
        self.size = self.size - 1
        self.heapifyDown(0, idealMovie)
        # return temp.getMovie()
        return temp
