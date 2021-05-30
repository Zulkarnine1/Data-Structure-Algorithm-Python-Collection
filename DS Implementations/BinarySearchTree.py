class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


class BinarySearchTree:

    def __init__(self):
        self.root = None


    def insert(self,x):
        new_node = Node(x)
        if not self.root:
            self.root = new_node
        else:
            currentNode = self.root
            while (True):
                if(x<currentNode.val):
                    # left
                    if(not currentNode.left):
                        currentNode.left = new_node
                        return self
                    else:
                        currentNode = currentNode.left
                else:
                    # Right
                    if (not currentNode.right):
                        currentNode.right = new_node
                        return self
                    else:
                        currentNode = currentNode.right




    def lookup(self,x):
        if not self.root:
            return None
        else:
            currentNode = self.root
            while (True):
                if x == currentNode.val:
                    return True
                else:
                    if (x < currentNode.val):
                        # left
                        if (not currentNode.left):
                            return False
                        else:
                            currentNode = currentNode.left
                    else:
                        # Right
                        if (not currentNode.right):
                            return False
                        else:
                            currentNode = currentNode.right

    # def remove(self,x):
    #     tar_node, parentNode = self.__remove_lookup__(self,x)
    #     if not tar_node:
    #         return False
    #     else:
    #         chosenParent = None
    #         # no right child
    #         if not tar_node.right:
    #             if not parentNode:
    #                 self.root = tar_node.left
    #             else:
    #                 if tar_node.val<parentNode.val:
    #                     parentNode.left = tar_node.left
    #                 elif tar_node.val>parentNode.val:
    #                     parentNode.right = tar_node.left
    #
    #             chosenOne = tar_node.right
    #             while True:
    #                 if chosenOne.left:
    #                     chosenOne = chosenOne.left
    #                 else:
    #                     break
    #         elif tar_node.left:
    #                 chosenOne = tar_node.left
    #                 while True:
    #                     if chosenOne.right:
    #                         chosenOne = chosenOne.right
    #                     else:
    #                         break
    #         tar_node.val = chosenOne.val
    #
    #
    #
    # def __remove_lookup__(self, x):
    #     if not self.root:
    #         return None, None
    #     else:
    #         currentNode = self.root
    #         parentNode = None
    #         while (True):
    #             if x == currentNode.val:
    #                 return currentNode, parentNode
    #             else:
    #                 if (x < currentNode.val):
    #                     # left
    #                     if (not currentNode.left):
    #                         return None, None
    #                     else:
    #                         parentNode = currentNode
    #                         currentNode = currentNode.left
    #                 else:
    #                     # Right
    #                     if (not currentNode.right):
    #                         return None, None
    #                     else:
    #                         parentNode = currentNode
    #                         currentNode = currentNode.right



tree = BinarySearchTree()
res = tree.insert(9)
print(res)
res = tree.insert(4)
print(res)
res = tree.insert(6)
print(res)
res = tree.insert(20)
print(res)
res = tree.insert(170)
print(res)
res = tree.insert(1)
print(res)

node = tree.lookup(9)
print(node)

node = tree.lookup(1)
print(node)

node = tree.lookup(21)
print(node)