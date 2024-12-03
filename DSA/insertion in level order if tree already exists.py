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

    def insertInLevelOrder(self,data):
        if not self.root:
            self.root=Node(data)

        else:
            # enqueue the root initially
            q_temp=queue.Queue(10)
            q_temp.put(self.root)
            
            # when position is found for data to be inserted
            # break loop right away
            while True:
                # dequeue node 
                res=q_temp.get()
                
                # if left child is not NULL
                # enqueue the left child 
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
        
if __name__ == "__main__":
    tree=Tree()
    for data in [1,3,5,7,9,11,13]:
        tree.insertInLevelOrder(data)
    
    tree.display(tree.root,0)