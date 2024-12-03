class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

def main():
    head=None
    
    # this is what happends inside the linked list class where the temp
    # variable is used over and over and the traversing variable is used to travel through all
    # the nodes
    temp=Node(1) 
    head=temp
    trav=head

    temp=Node(8)
    trav.link=temp
    trav=temp

    temp=Node(1)
    trav.link=temp
    trav=temp

    trav=head
    while trav!=None:
        print(trav.data)
        trav=trav.link


main()