# Linked list implementation
# 1. Needs init
# 2. Needs append
# 3. Needs prepend
# 4. Needs insert
# 5. Needs delete
# 6. Needs lookup
class Node:

    # For each node of the linked list O(1)
    def __init__(self, val):
        self.val = val
        self.next = None


class ZulkarsLinkedList:

    # For the linked list itself .... setting head, tail and length on start O(1)
    def __init__(self, val):
        newNode = Node(val)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    # Getting an element at an index O(n)
    def getElement(self,index):
        prev = self.head
        for i in range(index - 1):
            if prev:
                prev = prev.next
            else:
                print(f"Index {i}  out of range.")
                return None
        return prev.next.val

    # Setting an element at an index O(n)
    def setElement(self,index,val):
        prev = self.head
        for i in range(index - 1):
            if prev:
                prev = prev.next
            else:
                print(f"Index {i}  out of range.")
                return None
        prev.next.val = val
        return prev.next.val

    # Adding elements from the end of the list  O(1)
    def append(self,val):
        newNode = Node(val)
        newNode.next = None
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return newNode.val

    # Adding elements from the beginning of the list O(1)
    def prepend(self,val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.length +=1
        return newNode.val

    # Removing elements from the end of the list O(n)
    def pop(self):
        prev = self.head
        for i in range(self.length-2):
            if prev:
                prev = prev.next
            else:
                print(f"Index {i}  out of range.")
                return None
        self.tail = prev
        print(prev.val)
        val = prev.next.val
        del prev.next
        prev.next = None
        return val




    # Adding elements at specific index of the list
    def insert(self,index,val):
        newNode = Node(val)
        prev = self.head
        for i in range(index-1):
            if prev:
                prev = prev.next
            else:
                print(f"Index {i}  out of range.")
                return None
        if prev:
            next = prev.next
            prev.next = newNode
            newNode.next = next
            self.length += 1
            return newNode.val

    # Deleting element from specific element of the list
    def delete(self,index):
        prev = self.head
        for i in range(index - 1):
            if prev:
                prev = prev.next
            else:
                print(f"Index {i}  out of range.")
                return None
        delNode = prev.next
        joinNode = delNode.next
        prev.next = joinNode
        val = delNode.val
        del delNode
        self.length -= 1
        return val

    # Displaying all elements of the list
    def display_list(self):
        pointer = self.head
        while (pointer):
            print(pointer.val)
            pointer = pointer.next





ll = ZulkarsLinkedList(10)
ll.append(12)
# ll.display_list()
ll.prepend(5)
ll.display_list()
print("========")
ll.insert(2,2)
ll.insert(6,90)
ll.display_list()
print("========")
ll.delete(2)
ll.display_list()
print("========")
ll.setElement(1,20)
print(ll.getElement(1))
print("========")
ll.display_list()
ll.pop()
print("========")
ll.display_list()









