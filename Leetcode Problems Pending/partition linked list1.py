class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class llist:
    def __init__(self):
        self.front=None
        self.last=None

    def enqueue(self,data):
        temp=Node(data)
        if not self.front and not self.last:
            self.last=temp
            self.front=self.last
        else:
            self.last.next=temp
            self.last=self.last.next

    def display(self):
        if not self.front: # if front is empty that means that queue is empty
            return
        else:
            trav=self.front
            while trav:
                print(trav.data)
                trav=trav.next
    
    def partition(self):
        pass

# like quick sort a way to partition these elements is to have two pointers
# one to get the value greater or equal to the pivot
# and one to get the value less than pivot
# 1 -> 4 -> 3 -> 2 -> 5 -> 2
# pivot is 3
# 
# but in this problem partitioning elements
# must be in a order such that
# all elements on the left side of the pivot is lesser than pivot
# and all nodes 


def Main():
    ll=llist()
    ll.enqueue(1)
    ll.enqueue(2)
    ll.enqueue(3)
    ll.enqueue(4)
    ll.display()
Main()