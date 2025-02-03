class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Circll:
    def __init__(self):
        self.front=None
        self.last=None
    
    def append(self,data): # takes O(1) time
        temp=Node(data)
        if not self.front and not self.last: # 
            self.last=temp
            self.front=self.last
        else:
            self.last.next=temp # set the last nodes ptr section to the new node
            self.last=self.last.next # since last node now points to new node update last ptr
        self.last.next=self.front # set the new node ptr section to head

    def push(self,data):
        temp=Node(data)
        if not self.front and not self.last:
            self.front=temp # set front to new node
            self.last=self.front # set last to new node also which will stay unless last is deleted
        else:
            temp.next=self.front # set ptr section of new node to the front to prevent loss of list
            self.front=temp # set front to the new node
            self.last.next=self.front # set ptr section of last to new head of list

    def display(self): # the only function that takes O(n) time
        if not self.front: # means that list is still empty
            print("list is empty")
        else:
            trav=self.front
            while trav!=self.last:
                print(trav.data)
                trav=trav.next
            print(trav.data)

    

def Main():
    ll=Circll()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.display()
Main()
