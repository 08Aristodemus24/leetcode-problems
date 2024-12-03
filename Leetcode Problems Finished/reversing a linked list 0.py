class Node:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
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
        if not self.head:
            return
        else:
            trav=self.head
            while trav:
                print(trav.val)
                trav=trav.next

    def reverseList(self,head):
        trav=head
        trace=None
        conn=trav
        while trav:
            trav=trav.next
            conn.next=trace
            trace=conn
            conn=trav
        return trace

def Main():
    ll=Solution()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.head=ll.reverseList(ll.head)
    ll.display()

Main()



# simlest length case of a linked list can be if list only has one node
# which in this case we would only return

# 2
# we would have to find the last node
# 1 -> 2 -> 3
# once returned since current head is back at 1 make the returned pointer point to the head argument
# conn holds 2 
# use its link to point to the current head argument
# what if for the first node it is set automatically to None

# set an if statement to see if it is at first node
