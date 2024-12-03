class Node:
     def __init__(self,data=None):
        self.data=data
        self.link=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def insert_node(self,data):
        if not self.head:
            self.head=Node(data)

        else:
            trav=self.head
            while trav.link!=None:
                trav=trav.link
            trav.link=Node(data)


def printLinkedList(head):
    trav=head
    if not trav:
        return
    
    else:
        while trav!=None:
            print(trav.data)
            trav=trav.link

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)