# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
    
class Solution:
    def __init__(self):
        self.head=None
        
    def append(self,data):
        if self.head==None:
            self.head=ListNode(data)
        else:
            trav=self.head
            while trav.next!=None:
                trav=trav.next
            trav.next=ListNode(data)

    def display(self):
        if self.head==None:
            return
        else:
            trav=self.head
            while trav!=None:
                print(trav.val)
                trav=trav.next

    def mergeTwoLists(self,l1,l2):
        trav_0=l1
        trav_1=l2
        while trav_0!=None and trav_1!=None: # either one or both lists must run out in order to break out
            if trav_0.val>trav_1.val:
                self.append(trav_1.val)
                trav_1=trav_1.next
            else:
                self.append(trav_0.val)
                trav_0=trav_0.next
        if trav_0!=None:
            while trav_0!=None:
                self.append(trav_0.val)
                trav_0=trav_0.next
        else:
            while trav_1!=None:
                self.append(trav_1.val)
                trav_1=trav_1.next
        return self.head

def display(head):
    trav=head
    if trav==None:
        return
    else:
        while trav!=None:
            print(trav.val)
            trav=trav.next

def Main():
    result=Solution()
    l1=Solution()
    l2=Solution()
    l1.append(1)
    l1.append(2)
    l1.append(3)
    l2.append(2)
    l2.append(4)
    l2.append(5)
    ans=result.mergeTwoLists(l1.head,l2.head)
    display(ans)

    

Main()