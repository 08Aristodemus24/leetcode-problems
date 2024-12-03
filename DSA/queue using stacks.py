class QueueMethod1:
    def __init__(self,CAP=0):
        self.top=-1
        self.head1=[]

        # this stack has unlimited size 
        # for only pushing the elements
        # to be popped in stack 1
        self.head2=[]

        self.CAP=CAP

    # time complexity of push is O(n) in worst case
    def enqueue(self,data):
        if self.isFull():
            print("element not added")
            return False
        else:
            # if stack 1 is empty then push that one element
            if self.top==-1:
                self.top+=1
                self.head1.append(data)
            
            # if stack has one element or more then
            # pop all until empty then append/push to
            # stack 2
            else:
                # pop and remove all elements
                while self.head1:
                    popped=self.head1.pop()
                    self.head2.append(popped)
                    self.top-=1

                # append/push the value once all
                # elements have been popped
                self.head1.append(data)
                self.top+=1

                # push all elements once
                # again
                while self.head2:
                    popped=self.head2.pop()
                    self.head1.append(popped)
                    self.top+=1

    # time complexity of pop is O(1) in worst and best case
    def dequeue(self):
        if self.isEmpty():
            print("element not removed")
            return False
        else:
            # dequeue the element in stack by popping
            self.top-=1
            popped=self.head1.pop()
            return popped


    def isEmpty(self):
        return self.top==-1

    def isFull(self):
        return self.CAP-1==self.top

class QueueMethod2:
    def __init__(self,CAP=0):
        pass

    def enqueue(self,data):
        pass

    def dequeue(self):
        pass

    def isEmpty(self):
        pass

    def isFull(self):
        pass

def Main():
    queue=QueueMethod1(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.dequeue()
    queue.enqueue(6)
    print(queue.head1)


Main()
