from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
        
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length=listlength(head)
        
        if length==1 or length==0:
            return head

        k=k%length # optimize number of rotations
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
        while trav.next:
            trav=trav.next
        trav.next=head
        return temp
        
    
def listlength(head):
    length=0
    trav=head
    while trav:
        length+=1
        trav=trav.next
    return length

