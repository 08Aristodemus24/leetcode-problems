class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.length=0

class LList:
    def append(self,head,data):
        if not head:
            return Node(data)
        trav=head
        while trav.next:
            trav=trav.next
        trav.next=Node(data)

        # to accumulate the length each time
        # append is use d
        trav.next.length=1+self.getLength(trav)
        return head

    def getLength(self,head):
        if not head:
            return -1

        return head.length

    def display(self,head):
        trav=head
        while trav:
            print(trav.data,end=' ')
            print("height is %d"%(trav.length))
            trav=trav.next
        

    


if __name__ == "__main__":
    
    ll=LList()
    head=None
    head=ll.append(head,1)
    head=ll.append(head,2)
    head=ll.append(head,3)
    head=ll.append(head,4)
    head=ll.append(head,5)
    ll.display(head)