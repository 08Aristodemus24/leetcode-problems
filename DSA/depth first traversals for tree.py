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
            self._insert(self.root,data) 
            # helper function is used since instance attributes are used as arguments for the recursive function

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
        for i in range(self.COUNT[0],space): 
            print(end=" ")  
        print(root.data)  
  
        # Process left child  
        self.display(root.leftc,space)


def Main():
    tree=Tree()
    tree.insert(7)
    tree.insert(8)
    tree.insert(9)
    tree.insert(6)
    tree.insert(7)
    tree.insert(10)
    tree.insert(7)
    tree.insert(4)
    tree.insert(6)
    tree.display(tree.root,0)

Main()