class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class LL:
    def __init__(self): # important variables to keep track of
        self.head=None

    def append(self,data):
        if not self.head:
            self.head=Node(data)

        else:
            trav=self.head
            while trav.link!=None:
                trav=trav.link
            trav.link=Node(data)

    def display(self): # helper function is private function: _display
        self._display(self.head)

    def _display(self,head):
        if not head:
            return

        print(head.data,end=' ')
        self._display(head.link)

    def getIntersection(self,headA,headB):
        pass


# method 1: brute force running in O(n^2)

# method 2: multiple scans running O(n) two pointers
# if two linked lists have no intersection return NULL
# 
# length cases:
# 0 and 0 return NULL 
# 1 and 0 or 0 and 1 return NULL
# 1 and 1 check if intersection exists, if yes return node, no return NULL
# 
# -for corner cases while can be trav1 and trav2
# -since there is no way of telling what is the length of each list
# 