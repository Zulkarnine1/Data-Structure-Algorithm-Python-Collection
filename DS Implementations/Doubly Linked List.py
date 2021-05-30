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
        self.previous = None


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
        newNode.previous = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return newNode.val

    # Adding elements from the beginning of the list O(1)
    def prepend(self,val):
        newNode = Node(val)
        newNode.next = self.head
        newNode.previous = None
        self.head = newNode
        self.length +=1
        return newNode.val

    # Removing elements from the end of the list O(n)
    def pop(self):
        prev = self.tail.previous
        self.tail = prev
        val = prev.next.val
        del prev.next
        prev.next = None
        return val




    # Adding elements at specific index of the list
    def insert(self,index,val):
        if index>=self.length:
            print("Index out of range")
            return None
        newNode = Node(val)
        leftNode = None
        rightNode = None
        pointer = self.head
        for i in range(self.length):
            if i == index:
                leftNode = pointer.previous
                rightNode = pointer
                break
            else:
                pointer = pointer.next

        leftNode.next = newNode
        newNode.previous = leftNode
        newNode.next = rightNode
        rightNode.previous = newNode
        self.length += 1
        return newNode.val







    # Deleting element from specific element of the list
    def delete(self,index):
        if index>=self.length:
            print("Index out of range")
            return None
        leftNode = None
        rightNode = None
        pointer = self.head
        for i in range(self.length):
            if i == index:
                leftNode = pointer.previous
                rightNode = pointer.next
                break
            else:
                pointer = pointer.next

        leftNode.next = rightNode
        rightNode.previous = leftNode
        val = pointer.val
        del pointer
        self.length -= 1
        return val

    # Displaying all elements of the list
    def display_list(self):
        pointer = self.head
        while (pointer):
            print(pointer.val)
            pointer = pointer.next

    def reverse(self):
        l = self.head
        r = self.tail
        lc = 0
        rc = self.length-1
        while(lc<rc):
            temp = l.val
            l.val = r.val
            r.val = temp
            l = l.next
            r = r.previous
            lc+=1
            rc-=1





ll = ZulkarsLinkedList(1)
ll.append(10)
ll.append(16)
ll.append(88)
print("====")
# ll.display_list()
# ll.prepend(5)
# ll.display_list()
# print("========")
# ll.insert(2,2)
# ll.insert(6,90)
# ll.display_list()
# print("========")
# ll.delete(2)
# ll.display_list()
# print("========")
# ll.setElement(1,20)
# print(ll.getElement(1))
# print("========")
# ll.display_list()
# ll.pop()
# print("========")
ll.reverse()
ll.display_list()









