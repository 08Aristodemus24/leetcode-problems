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

if __name__ == "__main__":
    tree=Tree()
    for val in [1,2,3,4,5,6]:
        tree.insert(val)

    tree.display(tree.root,0)