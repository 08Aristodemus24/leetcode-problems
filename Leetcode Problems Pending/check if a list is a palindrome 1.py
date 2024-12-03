class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
        
class Solution:
    def __init__(self):
        self.head=None

    def append(self,data):
        if not self.head:
            self.head=ListNode(data)
        else:
            trav=self.head
            while trav.next:
                trav=trav.next
            trav.next=ListNode(data)
    
    def display(self):
        if not self.head:
            return 
        else:
            trav=self.head
            while trav:
                print(trav.val)
                trav=trav.next

    def reverse(self,head):
        trav=head
        conn=trav
        trace=None
        while trav:
            trav=trav.next # update trav first
            conn.next=trace # connect conn to trace which is currently None 
            trace=conn # set trace to conn since it will be the basis of conn to connect itself to the previous node
            conn=trav 
        return trace

    def isPalindrome(self,head):
        revd=Solution()
        trav_1=head
        while trav_1:
            revd.append(trav_1.val)
            trav_1=trav_1.next
        revd.head=self.reverse(revd.head)
        
        # loop through each element of reversed and original
        trav_0=revd.head
        trav_1=head
        while trav_1 and trav_0:
            if trav_0.val==trav_1.val: 
                trav_0=trav_0.next
                trav_1=trav_1.next
            else: # execute only when value of reversed and orig do not match
                return False
        return True    


def Main():
    ll=Solution()
    ll.append(1)
    ll.append(1)
    ll.append(2)
    ll.append(1)
    ll.display()
    print(ll.isPalindrome(ll.head))


Main()


# a palindrome is a list of values that when read in reverse it is also that same list of values
# 1,2,2,1 
# 1,2 not a palindrome since 2,1 is not equal to 1,2
# 1,2
# | |
# 2 1
# first element is not equal to first element in reversed order therefore not a palindrome
# until there is no element that isnt equal to each other keep checking each element

# 1,2,1
# 1,2,1 True

# 1,2,3,1
# 1,3,2,1 False

# 1,2,2
# 2,2,1 True

# method 1: reversing the list and checking with each element
# 