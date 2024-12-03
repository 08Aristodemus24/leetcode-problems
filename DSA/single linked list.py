

class Node:
    def __init__(self,data=None):
        self.data=data
        self.link=None

class LLM:
    def __init__(self):
        self.head=None # this is where we should set the head to None

    def __repr__(self):
        return "some object='{}'".format("object")
        
    def append(self,data):
        if not self.head: # however there is no way of knowing if a list is empty
            self.head=Node(data)

        else:
            trav=self.head # trav now has the attributes of self.head
            while trav.link!=None:
                trav=trav.link
            trav.link=Node(data)

    def display(self):
        if not self.head:
            print("list is empty")

        else:
            trav=self.head # we know that self.head with the attributes of class Node
            while trav.link!=None:
                print(trav.data,end=' ')
                trav=trav.link

    def length(self):
        self.count=0
        if not self.head:
            return 0

        else:
            trav=self.head
            while trav.link!=None:
               self.count+=1
               trav=trav.link
            return self.count
        
def main():

    ''' head must be initialized to a class because setting an object to None would create extra unecessary variables'''
    
    head=LLM() # note that head is not initialized here to None
    head.append(9) # this is similar to passing the head variable in functions in C
    head.append(1)
    head.append(2)
    head.append(4)
    head.append(3)
    head.append(5)
    head.append(6)
    head.append(8)
    head.append(7)
    head.append(0)
    head.display()
    print(head)
    
    #print("\n")
    #for obj in head.head.__dict__:
        #print(obj)

main()