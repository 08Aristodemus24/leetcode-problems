COUNT=[10]

class Cell:
    def __init__(self,data):
        self.data=data
        self.leftc=None
        self.rightc=None

class Tree:
    def __init__(self):
        self.root=None # this is where we initially set root as None

    def insert(self,node,data): 
        self.node=node # because root is initially None self.node will append the 
        if not self.node:
            self.node=Cell(data)
            return

        else:
            if data<=self.node.root.data:
                self.insert(self.node.leftc,data) 

            else:
                self.insert(self.node.rightc,data)

    def display(self,node,space):
        self.node=node
        if self.node is None:
            return
        
        space+=COUNT[0]

        self.display(self.node.rightc,space)

        print()  
        for i in range(COUNT[0], space): 
            print(end = " ")  
        print(self.node.root.data)  
  
        # Process left child  
        self.display(self.node.rightc,space)
 

def main():

    root=Tree()
    root.insert(root,7)
    root.insert(root,8)
    root.insert(root,9)
    root.insert(root,6)
    root.insert(root,10)
    root.insert(root,4)

    root.display(root,0)


main()