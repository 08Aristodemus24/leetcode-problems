class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

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

def length(head):
    if not head:
        return 0

    else:
        count=0
        trav=head
        while trav!=None:
            count+=1                
            trav=trav.next
        return count
    
def compare_lists(ptr1,ptr2): # pass each list head attributes in compare()
    val=1
    if length(ptr1)==length(ptr2):
        trav1=ptr1
        trav2=ptr2
        while trav1!=None:
            if trav1.data==trav2.data:
                trav1=trav1.next
                trav2=trav2.next
            else:
                val=0
                break
        
        if val==0:
            return 0
        return 1
    else:
        return 0



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()