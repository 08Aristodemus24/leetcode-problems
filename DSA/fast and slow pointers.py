class Cell:
    def __init__(self,data):
        self.data=data
        self.link=None

class Queue:
    length=-1 # initial value of length when queue is empty

    def __init__(self,size=None):
        self.rear=None # store value of rear element 
        self.front=None # store value of front element
        self.size=size

    def enqueue(self,data=None):
        if self.isfull():
            print("queue is full, "+str(data)+" not added")
        
        else:
            temp=Cell(data) # allocate cell
            if self.rear==None and self.front==None:
                self.rear=temp # point rear to temp
                self.front=self.rear # point front to temp
            
            else:
                self.rear.link=temp # connect link of current rear to new node
                self.rear=temp # set rear to new node

            self.length+=1 # increment value of length when enequeue is called

    def isempty(self):
        if self.length==-1: # queue is empty if length is -1 since it has no nodes
            return True
        else:
            return False

    def isfull(self):
        if self.length+1==self.size: # add one since length starts at 0 when node is added
            return True
        else:
            return False

    def traverse(self):
        slow=self.front
        fast=self.front
        while fast and (slow==None or fast.link): # must always be put in parentheses so condition can automatically end if at least one of the two is false since and is used
            fast=fast.link.link
            slow=slow.link
        print(slow.data)
        # goal is for slow to reach the end but fast to reach it the end faster
        # whatever node slow has stopped to when fast reaches end then that will be 
        # slows node
        
        # method:
        # both pointers must travel at the same time in one while loop
        # in linear time O(n)

        # idea:
        # start both slow and fast pointers at head

        
        # cases:
        # 1. length is 1 slow only traverses once, fast exceeds, once slow reaches NULL stop 1
        # 2. length is 2 slow only traverses once, fast reaches NULL so stop 1->2
        # 3. length is 3 slow only traverses once, fast reaches last node 1->2->3
        # however if fast traverses again it will exceed, and slow will not be NULL by then
        # so stop loop if fast is at last node and slow is not NULL, or fast is at NULL 
        # 4. length is 0 since slow is null and fast is NULL loop will not execute
        

def Main():
    queue=Queue(7)
    queue.enqueue(1)


    queue.traverse()

Main()