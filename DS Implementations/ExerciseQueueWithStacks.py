# Stack Implementation Using Array
class StackArray:

    def __init__(self):
        self.data = []
        self.length = 0


    def peek(self):
        if self.length>0:
            return self.data[self.length -1]

    def push(self,val):
        self.data.append(val)
        self.length += 1
        return self.data

    def pop(self):
        if self.length>0:
            val = self.data[self.length-1]
            self.data.pop()
            self.length -= 1
            return self.data

    def is_empty(self):
        if self.length <= 0:
            return True
        else:
            return False


class MyQueue:

    def __init__(self):
        self.tempStack = StackArray()
        self.perStack = StackArray()
        self.length = 0

    def push(self, x: int) -> None:
        if self.perStack.is_empty():
            self.perStack.push(x)
        else:
            for i in range(self.length+1):
                tempVal = self.perStack.peek()
                self.tempStack.push(tempVal)
                self.perStack.pop()

            self.perStack.push(x)

            for i in range(self.length):
                tempVal = self.tempStack.peek()
                self.perStack.push(tempVal)
                self.tempStack.pop()

            self.length += 1
            return x



    def pop(self) -> int:
        if self.perStack.is_empty():
            return None
        else:
            self.length -= 1
            x = self.perStack.pop()
            return x

    def peek(self) -> int:
        return self.perStack.peek()

    def empty(self) -> bool:
        return self.perStack.is_empty()

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
