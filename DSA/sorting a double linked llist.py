class Node:
    def __init__(self,data=None):
        self.left=None
        self.data=data
        self.right=None

class Dllist:
    length=0
    def __init__(self):
        self.head=None

    def append(self,data):
        temp=Node()
        if not self.head:
            self.head=temp
        else:
            trav=self.head
            while trav.right: # find last node
                trav=trav.right
            trav.right=temp
            trav.right.left=trav

    def display(self):
        if not self.head:
            print("list is empty")
        else:
            trav=self.head
            while trav:
                print(trav.data)
                trav=trav.right
    
    def mergesort(self):
        _mergesort()

    def _mergesort(head,lo,hi):
        mid=int(lo+hi)/2+1
        if lo>=hi:
            return
        _mergesort(head,lo,mid-1)
        _mergesort(head,lo,hi-mid)

        i=j=k=0
        trav=head
        while i!=mid and j!=hi-mid+1:
            if