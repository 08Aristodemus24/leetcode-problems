class Node:

    def __init__(self,char): # initialize arguments to NULL if you choose to not give an argument to an instance
        self.left=None
        self.char=char
        self.right=None 


class DLLM:
    def __init__(self): # this will create a node
        self.head=None
        self.last=None

    def append(self,data):

        if not self.head:
            self.head=Node(data)

            return self.head

        else:
            self.trav=self.head
            while self.trav.right!=None:
                self.trav=self.trav.right
            self.trav.right=Node(data) # connect right side to new node
            self.trav.right.left=self.trav # connect left side of new node to last node 
            
            return self.trav.right
            
    def display(self):
        if not self.head:
            print("list is empty")

        else:
            self.trav=self.head
            while self.trav!=None:
                print(self.trav.char,end='')
                self.trav=self.trav.right

    def backward(self,last):
       self.trav=last
       while self.trav!=None:
           print(self.trav.char,end='')
           self.trav=self.trav.left

    def length(self):
        self.count=0
        self.trav=self.head
        while self.trav!=None:
            self.count+=1
            self.trav=self.trav.right

        return self.count
        

def main():
    head=DLLM()
    last=head.append(5)
    last=head.append(1)
    last=head.append(4)
    last=head.append(2)
    last=head.append(3)
    last=head.append(3)
    last=head.append(3)
    last=head.append(3)
    last=head.append(3)
    last=head.append(3)
    last=head.append(3)
    

    head.display()
    print("\n")
    head.backward(last)
    print("\n")
    print(head.length())

    # since there are no pointers to replicate an address and connect it to other nodes
        
main()

