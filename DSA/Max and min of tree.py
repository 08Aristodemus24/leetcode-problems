import queue
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
                self._insert(root.rightc,data) # keep traversing until it reaches leaf node or last node before NULL
        else:
            if not root.leftc:
                root.leftc=Node(data)
            else:
                self._insert(root.leftc,data)

    def levelOrder(self):
        if self.root:
            q_temp=queue.Queue(10)
            stack=[]

            q_temp.put(self.root) # enqueue the first element in the tree which is the root node
            while not q_temp.empty(): # while q_temp is full that means that there are still elements to traverse
                res=q_temp.get() # dequeue element at the front and get its value 
                stack.append(res.data)

                # after dequeuing element
                if res.leftc: # if even one of these children is NULL dont enqueue anymore
                    q_temp.put(res.leftc)
                if res.rightc:
                    q_temp.put(res.rightc)
            return stack

    def maxNum(self):
        # this is if root is NULL
        if not self.root:
            return -1
        return self._maxNum(self.root)

    def _maxNum(self,root):
        if not root:
            return 0
        
        left_val=self._maxNum(root.leftc)
        right_val=self._maxNum(root.rightc)
        return self.maxOfThree(left_val,right_val,root.data)

    def minNum(self):
        if not self.root:
            return -1
        return self._minNum(self.root)

    def _minNum(self,root):
        # if we return 0 just like in the
        # max of a tree then 0 will just be the min
        # so initially when NULL is reached we have to return its current root.data
        if not root:
            return MAX
        
        # when values are returned compare
        # both values and return the max of the two
        left=self._minNum(root.leftc)
        right=self._minNum(root.rightc)
        return self.minOfThree(root.data,left,right)

    def maxOfThree(self,num1,num2,num3):
        if num1>=num2 and num1>=num3:
            return num1
        elif num2>=num1 and num2>=num3:
            return num2
        return num3

    def minOfThree(self,num1,num2,num3):
        if num1<=num2 and num1<=num3:
            return num1
        elif num2<=num1 and num2<=num3:
            return num2
        return num3

def Main():
    root=Tree()
    root.insert(7)
    root.insert(8)
    root.insert(9)
    root.insert(6)
    root.insert(3)
    root.insert(6)
    root.insert(10)
    root.insert(50)
    root.insert(7)
    root.insert(4)
    root.insert(1)
    print("values of tree are ",root.levelOrder())
    print("maximum and minimum value in the tree is %d & %d"%(root.maxNum(),root.minNum()))
    
Main()        
# problem:

# method:
# - we reach the farthest NULL value then we return 0
# - this can either be for the left and right child
# - so if we were to be at the last node once both 0's are returned
# we compare the three values and find the largest of the three

# idea:
# - we can first reach the depth of the farthest node
# - if we become NULL then we return since our only goal is to compare it to the one previously above it or the right side
# if ever there is one present
 


# figure out/drawbacks:
# - we can keep updating the max by going down but we have to pass in the current max 
# every single time so the current function call knows what is the max and compare it to
# its current number

# samples/cases:
# 1. if tree is just empty return nothing
# 2. if tree has at least one node
#           *
# set current max as 0
# assuming all the data in the tree is positive compare it to zero
# then update the current max if that number is greater than zero
# we set it to zero so because we assume that there will be no negative number present in the tree
# 3. if tree has more than one node
# - 3 nodes as a sample
#               *
#           *       *
#         0   0   0   0

