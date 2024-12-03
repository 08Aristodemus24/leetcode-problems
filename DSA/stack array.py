class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class StackLList:
    def __init__(self):
        self.head=None

    def push(self,data):
        temp=Node()
        temp.next=self.head
        self.head=temp

    def pop(self):
        popped=self.head.data

        # head pointer moves to next node
        self.head=self.head.next

        # returns popped element
        return popped 

    def isempty(self):
        return not self.head


class StackArray: 
    def __init__(self,CAP=0):
        # indicator if stack has an element or -1 if its empty
        self.top=-1 

        # initialize all elements to None times capacity
        self.head=[None]*CAP 
        self.CAP=CAP
        
    def push(self,data):
        if self.isfull():
            print("stack is full element not added")
        else:
            self.top+=1

            # initialize all elements to None times capacity
            self.head[self.top]=data

    def pop(self):
        if self.isempty():
            print("stack is empty nothing to be deleted")
        else:
            self.head[self.top]=None
            self.top-=1
            
    def isempty(self):
        return self.top==-1

    def isfull(self):
        return self.top==self.CAP-1

    

def Main():
    stack=StackArray()
    print(stack.head,"EMPTY =",stack.isempty())
    
Main()
        
    
    