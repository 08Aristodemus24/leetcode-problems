# constants will be used for determining the
# minimum value
from sys import maxsize as MAX 
MIN=-MAX-1

class Node:
    def __init__(self,data):
        self.data=data
        self.leftc=None
        self.rightc=None


class Tree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if not self.root:
            self.root=Node(data)
        else:
            self._insert(self.root,data)
            
    def _insert(self,root,data):
        if data>=root.data:
            if not root.rightc:
                root.rightc=Node(data)
            else:
                self._insert(root.rightc,data)
        else:
            if not root.leftc:
                root.leftc=Node(data)
            else:
                self._insert(root.leftc,data)

    def findMin(self):
        if not self.root:
            return -1
        return  self._findMin(self.root)

    def _findMin(self,root):
      
        # if we return 0 just like in the
        # max of a tree then 0 will just be the min
        # so initially when NULL is reached we have to return its current root.data
        if not root:
            return MAX
        
        # when values are returned compare
        # both values and return the max of the two
        left=self._findMin(root.leftc)
        right=self._findMin(root.rightc)
        return self.compareThree(root.data,left,right)

    def minOfThree(self,num1,num2,num3):
        if num1<=num2 and num1<=num3:
            return num1
        elif num2<=num1 and num2<=num3:
            return num2
        return num3


if __name__ == "__main__":
    tree=Tree()
    tree.insert(10)
    tree.insert(8)
    tree.insert(11)
    tree.insert(9)
    tree.insert(7)
    tree.insert(MIN)

    print(tree.findMin())
    
