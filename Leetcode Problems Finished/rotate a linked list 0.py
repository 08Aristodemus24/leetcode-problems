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
                print(trav.data,end=' ')
                trav=trav.next

    def rightRotate(self,head,k):
        length=listLen(head)
        if length==0 or length==1:
            return head

        k=k%length
        if k==0 or k==length:
            return head

        i=0
        trav=None
        while i<length-k:
            if not trav:
                trav=head
            else:
                trav=trav.next
            i+=1
        temp=trav.next # connect temp to new head
        trav.next=None # set the previous node to the new last node
        trav=temp 
        while trav.next: # traverse until the last node
            trav=trav.next
        trav.next=head
        return temp


# auxiliary functions
def listLen(head):
    length=0
    trav=head
    while trav:
        length+=1
        trav=trav.next
    return length

def Main():
    ll=llist()
    ll.enqueue(1)
    ll.enqueue(2)
    ll.enqueue(3)
    ll.enqueue(4)
    ll.enqueue(5)
    ll.front=ll.rightRotate(ll.front,100000000000009)
    ll.display()
    

Main()