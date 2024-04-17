import sys

class Heap:
    # Citation: Geeks for Geeks (we will change this is just a skeleton to take up space for the time being)
    def __init__(self, max):
        # change some stuff as needed this is a basic heap structure
        # array based heap implementation
        self.maxsize = max
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    def getParent(self, child):
        return child // 2

    def leftChild(self, index):
        return 2 * index

    def rightChild(self, index):
        return 1 + (2 * index)

    def isLeaf(self, index):
        return index*2 > self.size

    def swap(self, a, b):
        pass

    def heapify(self, index):
        # build a heap in place
        pass
