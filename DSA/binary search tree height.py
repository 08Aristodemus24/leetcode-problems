import queue

class Node:
    def __init__(self,data=None):
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
            self._insert(self.root,data) 
            # this is the helper method for insert since recursion 
            # cannot be done directly especially if attribute passed will be changed

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

    def print2DUtil(self,root,space): 
        # Base case  
        if not root: 
            return
  
        # Increase distance between levels  
        space+=self.COUNT[0] 
  
        # Process right child first  
        self.print2DUtil(root.rightc,space)  
  
        # Print current node after space  
        # count
        print()  
        for _ in range(self.COUNT[0],space): 
            print(end=" ")  
        print(root.data)  
  
        # Process left child  
        self.print2DUtil(root.leftc,space)

    def maxHeight(self):
        return self._height(self.root)

    def _height(self,root):
        if not root: # when base case is reached all 1's will be accumulated and build the height of the tree
            return 0
        left_max=1+self._height(root.leftc) # left will be compared to rights height and return the height of larger value
        right_max=1+self._height(root.rightc)
        if left_max>=right_max: # there is no telling what the depth of both subtrees will be, either left or right is the largest
            return left_max
        return right_max

    def maxWidth(self):
        return self._width(self.root)

    def _width(self,root):
        if not root:
            return 

        


# problem:

# method:

# idea:
# when first depth is found set it as the current max
# when 2nd depth is found compare it always to the current max
# if that 2nd depth is > than cur max then change cur max to/= depth
# 

# figure out:

# cases:
# 1. if tree is empty return 0
# 2. root only then return 1 max is incremented by one

# samples:
#               *
#         *          *
#      *     *    *     *
#    *   * *   *
#           *  
# as left side goes down max is incremented 
# when left reaches NULL return
# right side is now proceessed but we see it is still NULL
# so we return from the function
# if right is not NULL then we 

def Main():
    root=Tree()
    root.insert(7)
    root.insert(8)
    root.insert(9)
    root.insert(6)
    root.insert(3)
    root.insert(6)
    root.insert(10)
    root.insert(0)
    root.insert(7)
    root.insert(4)
    root.insert(1)
    root.print2DUtil(root.root,0)
    print("the tree's max height is %d"%(root.maxHeight()))
    
Main()        
