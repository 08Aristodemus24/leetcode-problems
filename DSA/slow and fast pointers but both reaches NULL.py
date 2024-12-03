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
        i,j=0,0 # this keeps the count of both pointers number of stops per node
        slow,fast=self.front,self.front

        while slow or fast: # stops when both pointers reach NULL
            if fast: # if fast is at NULL this will not execute anymore
                if not fast.link:
                    fast=fast.link
                else:
                    fast=fast.link.link
                j+=1
            slow=slow.link # slow must reach NULL no matter what 
            i+=1
        return i,j
        # problem:

        # method:

        # idea:
        # create an if statement that handles fast pointers that reach the last node because of even length so that they can reach NULL
        # create also an if statement that handles slow pointers that are not yet NULL and while fast has already finished

        # cases:
        # length is 0 so while loop never executes
        # length is 1 fast will be out of bounds since it is at last if while executes but slow is at last node and is not yet null so loop never executes 1
        # length is 2 fast reaches NULL but slow is at last node, stop looping fast and loop only slow until slow reaches NULL 1->2
        # length is 3 fast reaches last node but one more would be out of bounds and slow is not yet at NULL
        # loop only slow if fast is now NULL 
        # if fast is at last node then update only once
        # check inside fast is at last if yes then update fast once\
        # else then update fast twice

        # figure out:
        # sample:
        # 1->2->3
        #    ^  ^
        #    s  f
        # if fast.link then update only once
        # fast is now NULL but because fast or slow while still keep looping but only slow is moving
        # while slow or fast
        # if slow 
        # if fast null then dont execute any more only slow


def Main():
    queue=Queue(7)
    queue.enqueue(1)
    queue.enqueue(1)
    queue.enqueue(1)
    queue.enqueue(1)
    queue.enqueue(1)
    queue.enqueue(1)
    queue.enqueue(1)
    slow,fast=queue.traverse()
    print("fast:%d is %d times faster than slow:%d"%(fast,slow/fast,slow))

Main()