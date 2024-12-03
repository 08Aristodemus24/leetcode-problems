from random import*

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
        # if front is empty that means that queue is empty
        trav=self.front 
        while trav:
            print(trav.data,end=' ')
            trav=trav.next

    def find(self,head,index):
        i=0
        trav=head
        while i<index:
            trav=trav.next
            i+=1
        return trav

    def length(self,head):
        length=0
        trav=head
        while trav:
            length+=1
            trav=trav.next
        return length
        
    def mergesort(self,head):
        # find the last node of the list
        # and pass it to the funciton as
        # the higher index node of the list
        last=self.find(head,self.length(head)-1)

        # call merge sort and pass 
        self._mergesort(head,last)
    
    def _mergesort(self,head,last):
        # find the midpoint number of the list
        mid=(self.length(head)//2)-1

        # return if either head is NULL or if head and last is equal
        # which indicates that list size down to one
        if head==last: 
            return
        
        # find the middle
        middle=self.find(head,mid)
        
        # declare reference to middle.next
        mid_head=middle.next

        # delete the connection of middle and its link
        middle.next=None

        # process left side from 0 to mid
        # process right side from mid to last
        self._mergesort(head,middle) 
        self._mergesort(mid_head,last) 

        # set the 1st pointer to the head
        # and the 2nd to the middle node
        trav1=head
        trav2=mid_head

        # create a class that will use a linked list
        temp=llist()
        while trav1 and trav2:
            if trav1.data>trav2.data:

                # append the element in the tem
                # linked list
                temp.enqueue(trav2.data) 
                trav2=trav2.next
            else:
                temp.enqueue(trav1.data)
                trav1=trav1.next

        # append all remaining nodes 
        if trav1:
            while trav1:
                temp.enqueue(trav1.data)
                trav1=trav1.next
        else:
            while trav2:
                temp.enqueue(trav2.data)
                trav2=trav2.next
        
        # use the temp list to change all the nodes in
        # original linked list
        # connect the middle to the mid head
        middle.next=mid_head

        trav1=temp.front
        trav2=head
        while trav1:
            trav2.data=trav1.data
            trav1=trav1.next
            trav2=trav2.next
        
if __name__ == "__main__":
    ll=llist()

    for _ in range(50):
        ll.enqueue(randint(0,20))
    ll.mergesort(ll.front)

    ll.display()






        