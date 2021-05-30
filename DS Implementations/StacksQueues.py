# Linked List node class

class Node:

    def __init__(self,val=None):
        self.val = val
        self.next = None



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


# Stack Implementation Using Linked List
class StackLinkedList:


    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0


    def peek(self):
        if self.top:
            return self.top.val

    def push(self,val):
        node = Node(val)
        if self.top == None:
            node.next = None
        else:
            node.next = self.top
        if self.bottom == None:
            self.bottom = None
        self.top = node
        self.length += 1
        return val

    def pop(self):
        if self.top:
            if self.top == self.bottom:
                self.bottom = None
            target = self.top
            val = target.val
            self.top = self.top.next
            del target
            self.length -= 1
            return val

    def is_empty(self):
        if self.length <= 0:
            return True
        else:
            return False

stack1 = StackArray()
print(stack1.push("Google"))
print(stack1.push("Udemy"))
print(stack1.push("Discord"))
print(stack1.peek())
print(stack1.pop())
print(stack1.peek())
print(stack1.is_empty())
print(stack1.pop())
print(stack1.pop())
print(stack1.is_empty())
print(stack1.peek())
print(stack1.pop())


 # ============= Queues Implementation =============

class Queue:


    def __init__(self):
         self.first = None
         self.last = None
         self.length = 0


    def peek(self):
        if self.first:
            return self.first.val

    def enqueue(self, val):
        node = Node(val)
        if self.last == None:
            self.last = node
            self.first = node
        else:
            self.last.next = node
            self.last = node

        self.length += 1
        return val



    def dequeue(self):
        if self.first:
            if self.first.next:
                temp = self.first
                self.first = temp.next
                val = temp.val
                del temp
                self.length -= 1
                return val
            else:
                temp = self.first
                val = temp.val
                self.first = None
                self.last = None
                del temp
                self.length -= 1
                return val




    def is_empty(self):
        if self.length <= 0:
            return True
        else:
            return False


print("========== Queue =========")
q1 = Queue()
print(q1.enqueue("Joy"))
print(q1.enqueue("Matt"))
print(q1.enqueue("Pavel"))
print(q1.enqueue("Samir"))
print(q1.peek())
print(q1.dequeue())
print(q1.peek())
print(q1.is_empty())
print(q1.dequeue())
print(q1.dequeue())
print(q1.is_empty())
print(q1.peek())
print(q1.dequeue())
print(q1.peek())

# Implement queues using stacks



