COUNT=[10]

class Node:
    def __init__(self,data):
        self.data=data
        self.leftc=None
        self.rightc=None


class Tree:
    def __init__(self):
        self.root=None

    def icreatetree(self,data):
        trav=trace=self.root

        if not self.root:
            self.root=Node(data)

        else:
            while True: # find the node position where the data will be stored 
                if data<=trav.data:
                    trav=trav.leftc
                    if not trav: # if trav detects None ahead break out of loop
                        break
                    trace=trace.leftc

                else:
                    trav=trav.rightc
                    if not trav:
                        break
                    trace=trace.rightc
            if data<=trace.data:
                trace.leftc=Node(data)
            else:
                trace.rightc=Node(data)

    def rcreatetree(self,data):
        if not self.root:
            self.root=Node(data)

        else:
            if data<=self.root.data:
                pass                
            else:
                pass

    def print2DUtil(self,root,space) : 
  
        # Base case  
        if (root == None) : 
            return
  
        # Increase distance between levels  
        space += COUNT[0] 
  
        # Process right child first  
        self.print2DUtil(root.rightc,space)  
  
        # Print current node after space  
        # count  
        print()  
        for i in range(COUNT[0],space): 
            print(end = " ")  
        print(root.data)  
  
        # Process left child  
        self.print2DUtil(root.leftc,space)            

    def display(self):
        pass

def main():

    root=Tree()
    root.icreatetree(0)
    root.icreatetree(1)
    root.icreatetree(-1)
    root.icreatetree(2)
    root.print2DUtil(root.root,0)
    

main()
