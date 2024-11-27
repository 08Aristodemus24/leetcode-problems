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

        k= k % length # optimize number of rotations
        if k == 0 or k == length:
            return head
        
        i = 0
        trav = None
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
    length = 0
    trav = head
    while trav:
        length += 1
        trav = trav.next
    return length

def display(head):
    curr = head
    while curr != None:
        print(curr.val)
        curr = curr.next

def reverse(head):
    # idea:
    # to get 3 to point to 2, to get 2 to point to 1 and to get 1 to point to null
    # I need to keep track of the previous nodes by using a stack, because I need
    # 2 be processed first then 1 and this is how a stack works its first in last out
    # 2, 1 so when we loop through 1 then 2, 1 will get stored first then 2
    # we want to stop at 3 and by this time we would have our stack be [1, 2] already


    # cases:
    # 1->2->3->null
    # 1->null

    # Initialize three pointers: curr, prev and next
    curr = head
    prev = None

    # Traverse all the nodes of Linked List
    # pattern is 
    # 1
    # 2
    # 3
    while curr is not None:
        print(f'current iteration {curr.val}')
        # Store next
        # curr.next is 2
        # curr.next is 3
        next_node = curr.next

        # Reverse current node's next pointer
        # curr.next at iteration 1 will be None
        # curr.next at iteration 2 will be 1
        curr.next = prev

        # Move pointers one position ahead
        prev = curr
        curr = next_node

    # Return the head of reversed linked list
    return prev



    
class LinkedList:
    def __init__(self):
        self._head = None

    def insertAtBegin(self, data):
        new_node = ListNode(data)
        if self._head is None:
            self._head = new_node
        else:
            new_node.next = self._head
            self._head = new_node

    @property
    def head(self):
        return self._head

    

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insertAtBegin(5)
    linked_list.insertAtBegin(4)
    linked_list.insertAtBegin(3)
    linked_list.insertAtBegin(2)
    linked_list.insertAtBegin(1)
    display(linked_list.head)
    new_head = reverse(linked_list.head)
    display(new_head)

