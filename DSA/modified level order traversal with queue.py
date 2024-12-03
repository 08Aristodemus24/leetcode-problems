

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

    def levelOrder(self):
        if self.root:
            q_temp=[]
            result=[]
            root=self.root
        
            q_temp.append(root) # enqueue the first element in the tree which is the root node
            while q_temp: # while q_temp is full that means that there are still elements to traverse
                res=q_temp.pop(0) # dequeue element at the front and get its value
                result.append(res)
                #print(res.data,end=' ')

                # after dequeuing element
                if res.leftc: # if even one of these children is NULL dont enqueue anymore
                    q_temp.append(res.leftc)
                if res.rightc:
                    q_temp.append(res.rightc)
        return result

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

def Main():
    tree=Tree()
    tree.insert(7)
    tree.insert(8)
    tree.insert(6)
    tree.insert(9)
    tree.insert(3)
    tree.insert(5)
    tree.insert(9)
    tree.insert(6)
    tree.insert(2)
    tree.insert(7)
    tree.display(tree.root,0)
    for items in tree.levelOrder():
        print(items)
    
    

Main()
