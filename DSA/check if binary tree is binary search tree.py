import queue

class Node:
    def __init__(self,data):
        self.data=data
        self.leftc=None
        self.rightc=None

class Tree:
    def __init__(self):
        self.root=None
        self.COUNT=[10]

    def insert(self,data):
        if not self.root:
            self.root=Node(data)

        else:
            # note that all the nodes are enqueued in
            # level order so all nodes will be checked
            # sequentially and when one is NULL insert is done
            q_temp=queue.Queue(10)
            q_temp.put(self.root)

            while True:
                # dequeue the node from the queue
                # check the children of the node if either
                # one of them is a NULL
                res=q_temp.get()
                if not res.leftc:
                    res.leftc=Node(data)
                    break
                else:
                    q_temp.put(res.leftc)

                if not res.rightc:
                    res.rightc=Node(data)
                    break
                else:
                    q_temp.put(res.rightc)

    def display(self,root,space): 
        # Base case  
        if not root: 
            return
 
        # Increase distance between levels  
        space+=self.COUNT[0] 
  
        # Process right child first  
        self.display(root.rightc,space)  
  
        # Print current node after space  
        # count
        print()  
        for _ in range(self.COUNT[0],space): 
            print(end=" ")  
        print(root.data)  
  
        # Process left child  
        self.display(root.leftc,space)

    def isBST(self):
        return self._isBST(self.root)

    def _isBST(self,root):
        if not root:
            return True
        elif not root.leftc and not root.rightc:
            return True
        elif root.leftc.data<root.data<=root.rightc.data:
            return True
        else:
            return False
        


if __name__ == "__main__":
    tree=Tree()
    tree.insert(8)
    tree.insert(5)
    tree.insert(9)
    tree.insert(4)
    tree.insert(5)
    tree.insert(8)
    tree.insert(10)
    tree.insert(1)
    tree.insert(3)

    tree.display(tree.root,0)


# problem:
# given a binary tree
# check if it is a binary tree
# a binary tree we know has its nodes 
# in certain constraints such as
# a root nodes children left and right
# must be less than and greater than or equal
# to the root respectively

# method:

# idea:
# - recurse starting from the root 
# - check if values of left < root <= right


# cases/samples:
# 1. if root is NULL just return true
# 2. if root has no children return true
# 3. if root has children check if left < root <= right
# - recurse left first
# - check again if root is null has no children 

# figure out:

