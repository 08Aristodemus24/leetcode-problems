from random import*

class Node:
    def __init__(self,data):
        self.val=data
        self.next=None

class llist:
    def __init__(self):
        self.head=None

    def append(self,data):
        if not self.head:
            self.head=Node(data)
        else:
            trav=self.head
            while trav.next:
                trav=trav.next
            trav.next=Node(data)

    def display(self):
        trav=self.head
        while trav:
            print(trav.val,end=' ')
            trav=trav.next

    def findmid(self,head):
        fast,slow=head,head
        while fast and (slow==None or fast.next):
            fast=fast.next.next
            slow=slow.next
        return slow

    def findlast(self,head):
        trav=head
        while trav.next:
            trav=trav.next 
        return trav
    
    def length(self,head):
        length=0
        trav=head
        while trav:
            length+=1
            trav=trav.next
        return length            

    def mergesort(self,head):
        last=self.findlast(head)
        self._mergesort(head,last)

    def _mergesort(self,head,last):
        if head==last:
            return

        middle=self.findmid(head)
        mid_next=middle.next
        middle.next=None

        self._mergesort(head,middle)
        self._mergesort(mid_next,last)

        trav1,trav2=head,mid_next
        temp=llist()
        while trav1 and trav2:
            if trav1.val>trav2.val:
                temp.append(trav2.val)
                trav2=trav2.next
            else:
                temp.append(trav1.val)
                trav1=trav1.next

        if trav1:
            while trav1:
                temp.append(trav1.val)
                trav1=trav1.next
        else:
            while trav2:
                temp.append(trav2.val)
                trav2=trav2.next
        
        middle.next=mid_next
        trav1,trav2=temp.head,head
        while trav1:
            trav2.val=trav1.val
            trav1=trav1.next
            trav2=trav2.next


if __name__ == "__main__":
    ll=llist()
    ll.append(9)
    ll.append(6)
    ll.append(5)
    ll.append(4)
    ll.append(1)
    ll.append(8)
    ll.display()
    print()
    ll.mergesort(ll.head)
    ll.display()

        


