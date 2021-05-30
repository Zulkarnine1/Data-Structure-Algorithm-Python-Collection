class ZulkarsArray:

    # Init O(1)
    def __init__(self):
        self.data = {}
        self.length = 0

    # Get length O(1)
    def getLength(self):
        return self.length

    # Get element O(1)
    def getElement(self, index):
        if (index in self.data):
            return self.data[index]
        else:
            return None

    # Get array O(1)
    def get_array(self):
        return self.data

    # Modify element O(1)
    def modify(self, i, e):
        self.data[i] = e
        return self.data[i]

    # Push an element O(1)
    def push(self, element):
        self.data[self.length] = element
        self.length += 1
        return self.length

    # Insert element at certain index O(n)
    def insert(self, index, element):
        self.shift_others_on_insert(index)
        self.data[index] = element
        return element

    # Part of insert method
    def shift_others_on_insert(self, i):
        for i in range(self.length + 1, i):
            self.data[i] = self.data[i - 1]

        self.length = self.length + 1

    # Pop an element from the end O(1)
    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length = self.length - 1
        return lastItem

    # Delete element from certain index O(n)
    def delete(self, i):
        item = self.data[i]
        self.shift_others_on_delete(i)
        return item

    # Part of delete method
    def shift_others_on_delete(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]

        del self.data[self.length - 1]
        self.length = self.length - 1


array1 = ZulkarsArray()
array1.push("x")
array1.push("y")
array1.push("c")
array1.push("a")
array1.push("e")
array1.pop()
array1.delete(1)
print(array1.get_array())
array1.insert(1, "p")
print(array1.get_array())
array1.getLength()
array1.modify(0, "y")
print(array1.get_array())