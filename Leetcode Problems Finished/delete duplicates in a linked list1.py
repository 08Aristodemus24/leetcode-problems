class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

# removedup takes head as argument only
# since list is sorted a linear scan will do
# if head is NULL return
# use trav and conn for traversing and connecting

# length cases
# 1. list has only one node or no nodes just return
# 2. list has 2 nodes
#   -may have duplicates
# 3. list has 3 nodes
#   -may have duplicates at the end
#   -may have duplicates at the head
# 4. list has 6 or more nodes
#   -may have duplicates at the head,middle,end

class SinglyLinkedList():
    def __init__(self):
        self.head=None

    def insert_node(self,data):
        if not self.head:
            self.head=Node(data)

        else:
            trav=self.head
            while trav.next!=None:
                trav=trav.next
            trav.next=Node(data)

def removeDuplicates(head): # note that passed argument is an attribute of the linked list class
    trace=head
    trav=head.next
    conn=None
    if not head or head.next==None:
        return head
    
    else:
        # if list has null at the end
        while trav!=None:
            if trace.data==trav.data:
                conn=trace
                if trav.next==None:
                    trace=trace.next
                else:
                    trav=trav.next
                    trace=trace.next
                trav=trav.next
                trace=trace.next
                conn.next=trace # delete node

            else: # update trace and trav once and keep moving pointers
                trace=trace.next
                trav=trav.next
        
    return head

def display(head):
    trav=head
    if not head:
        return

    else:
        while trav!=None:
            print(trav.data)
            trav=trav.next


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    #t = int(input())

    #for t_itr in range(t):
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    display(llist.head)    
    llist1 = removeDuplicates(llist.head)
    print("\n")
    display(llist1)