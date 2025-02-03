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

    def reverse(self):
        self.head = self._reverse(self.head)

    def _reverse(self,head):
        if not head or not head.link:
            return head

        conn = self._reverse(head.link) # head is returned here
        head.link.link = head
        head.link = None
        return conn
            
            
    def length(self):
        length=0
        trav=self.head

        while trav!=None:
            length+=1
            trav=trav.link
        
        return length


def main():

    head=LL()
    head.append(1)
    head.append(2)
    head.append(3)
    head.append(4)
    head.append(5)
    head.display()
    print("\n")
    head.rreverse()
    head.display()

main()