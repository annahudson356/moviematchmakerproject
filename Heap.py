class Heap:
    def __init__(self):
        self.size = 0
        self.heap_arr = []

    def getArr(self):
        return self.heap_arr

    def heapifyDown(self, index, idealMovie):
        l = (index * 2) + 1
        r = (index * 2) + 2
        biggest = index
        if l < self.size and self.heap_arr[l].getSimilarity(idealMovie) > self.heap_arr[biggest].getSimilarity(idealMovie):
            biggest = l
        if r < self.size and self.heap_arr[r].getSimilarity(idealMovie) > self.heap_arr[biggest].getSimilarity(idealMovie):
            biggest = r
        if biggest != index:
            self.heap_arr[index], self.heap_arr[biggest] = self.heap_arr[biggest], self.heap_arr[index]
            self.heapifyDown(biggest, idealMovie)

    def extractMax(self, idealMovie):
        # Inspired by Programming Quiz 6
        temp = self.heap_arr[0]
        self.heap_arr[0] = self.heap_arr[self.size-1]
        self.size = self.size - 1
        self.heapifyDown(0, idealMovie)
        return temp.getMovie()