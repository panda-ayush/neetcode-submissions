class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity #O(n) where n is capacity

    def get(self, i: int) -> int: #O(1)
        return self.arr[i] #assuming i is always valid

    def set(self, i: int, n: int) -> None:#O(1)
        self.arr[i] = n

    def pushback(self, n: int) -> None: #O(n)
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int: #O(1)
        self.size -= 1
        temp = self.arr[self.size]
        del self.arr[self.size]
        return temp

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        for i in range(self.size): #O(n)
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity