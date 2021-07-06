# Binary Search Tree Implementation

# Check the BinarySearchTree class functions to get the BFS Implementation

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

    def breadth_first_search(self):
        curr_node = self.root
        ans = []
        q = []
        q.append(curr_node)
        while(len(q)>0):
            curr_node = q[0]
            q = q[1:]
            ans.append(curr_node.val)
            if(curr_node.left):
                q.append(curr_node.left)
            if(curr_node.right):
                q.append(curr_node.right)

        return ans

    def breadth_first_search_recur(self,q,l):
        if(len(q)==0):
            return l

        curr_node = q[0]
        q = q[1:]
        l.append(curr_node.val)
        if (curr_node.left):
            q.append(curr_node.left)
        if (curr_node.right):
            q.append(curr_node.right)

        return self.breadth_first_search_recur(q,l)





tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(15)
tree.insert(170)
tree.insert(1)
tree.lookup(9)
node = tree.lookup(1)
print(node)
node = tree.lookup(21)
print(node)
ans = tree.breadth_first_search()
print(ans)
ans = tree.breadth_first_search_recur([tree.root],[])
print(ans)
