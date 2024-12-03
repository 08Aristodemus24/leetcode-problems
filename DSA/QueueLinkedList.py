class Cell:
    def __init__(self,data):
        self.data=data
        self.link=None

class Queue:
    def __init__(self):
        self.rear=None # store value of rear element 
        self.front=None # store value of front element

    def enQueue(self,data=0):
        temp=Cell(data) # allocate cell
        if self.rear==None and self.front==None:
            # point rear and front to temp
            self.front=self.rear=temp 
            self.front=self.rear 
            
        else:
            # connect link of current rear to new node
            self.rear.link=temp 
            self.rear=temp

    def deQueue(self):
        if self.rear==None and self.front==None: # rear cannot be None while front has a value, both must be None
            return
        
        elif self.rear==self.front:
            self.front=self.rear=None

        else:
            self.front=self.front.link

    def display(self):
        if self.front==None:
            print("queue is empty")

        else:
            trav=self.front
            while trav!=None:
                print(trav.data,end=' ')
                trav=trav.link
            print("\n")
        
    def isEmpty(self):
        return self.front==None and self.rear==None



def main():

    # unlike an array implementation of a queue
    # a queue can be a circular array which:
    # - does not waste space when dequeue is performed
    # since extra space can be used when enQueue is performed
    # - all operations are O(1)
    # - but size is static and cannot be changed

    # a queue can use a counting variable which :
    # - does waste space since yes we can decrease/increase
    # the space when we deQueue/enQueue but in actuality
    # as we deQueue we just move the front to the next element
    # which does not really delete the extra space
    # - all operations are O(1)
    # - there is wasted space 

    # a queue can use a counting variable which:
    # - still wastes resources such as time
    # since it when it uses deQueue yes the the space is
    # saved but it takes O(n) since it pops at the first element
    # and all elements have to be shifted to return array to normal
    queue=Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    queue.display()

main()
