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

    def removeElements(self,head,val):
        trav=head
        trace=None
        while trav:
            if trav==head:
                if trav.data==val: # if trav is still at first node
                    head=head.next # set head to new head
                    trav=head
                else: 
                    trace=head
                    trav=trav.next
            else:
                if trav.data==val:
                    trav=trav.next
                    trace.next=trav
                else:
                    trav=trav.next
                    trace=trace.next       
        return head



def Main():
    ll=llist()
    ll.enqueue(1)
    ll.enqueue(1)
    ll.enqueue(2)
    ll.enqueue(3)
    ll.enqueue(4)
    ll.front=ll.removeElements(ll.front,3)
    ll.display()

Main()

# method 1: linear scan one pointer
# if the value is of the linked list is equal to the target val then delete
# adjacency cases:
# duplicate 1,2,2,3,4 delete 2
# - the pointer is at 2 then delete
# - the only way to connect 1 to the next node is by stopping the pointer at one
# - so check if ptr->link->data is val
# - but since this will not work with the last node
# - always check if traversal has reached the last node
# - ptr->link
# - check one final time if it has the value that needs to be deleted for the final node
# 
# method 2: linear scan two pointers
# take the above method but apply it to the two pointers trav and trace
# trace will connect and trav will check if the value is equal to the val
# since there is no way of telling if threre are duplicates
# the list may have more than 2 duplicates of the val
# so in the linear scan we do the ff
# 1,2,3,3,3,4
#   ^ ^
# check if trav has encountered a val
# trav moves on 
# and trav then again checks if there is a val
# yes move on
# no connect trace to trav right away
# after connection move trav and trace again

# length cases:
# 0 return head
# 1 either delete the node because of val or return head

# 2 set trav to first node
# check
# if found val move to the next node
# else move trav and set trace to first node
# check again

# yes then move again
# connect head to trav

# val location cases:
# at first node then connect head to the next nonval node else move 
# middle connect trace to nonval trav
# last still connect trace to nonval trav which is now NULL
 
