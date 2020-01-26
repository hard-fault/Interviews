class QuickSort():
    def sort(self, list):
        self._quickSort(list, 0, len(list) - 1)
        return list
    
    def _quickSort(self, list, low, high):
        if low < high:
            p = self._partition(list, low, high)
            self._quickSort(list, low, p - 1)
            self._quickSort(list, p + 1, high)
    
    def _getPivot(self, list, low, high):
        return high

    def _partition(self, list, low, high):
        border = low - 1
        pivot = self._getPivot(list, low, high)

        for i in range(low, high):
            if list[i] <= list[pivot]:
                border += 1
                list[border], list[i] = list[i], list[border]
        
        list[pivot], list[border + 1] = list[border + 1], list[pivot]
        return (border + 1)

quickSort = QuickSort()
list = [8,3,6,4,12,7]
print (quickSort.sort(list))