class CircQueue:
    def __init__(self,length=0):
        self.front=-1


class Queue:
    def __init__(self,length=0):
        # both front and rear have
        # intial values of -1 or None
        self.front=-1
        self.rear=-1
        self.length=length
        # initialize queue to nothing
        self.queue=[]  
        self.cur_len=0

    def enqueue(self,data):
        if self.isfull():
            print("queue is full")

        elif self.front==-1 and self.rear==-1:
            self.queue.append(data)
            # set front and rear to first element added
            self.front+=1
            self.rear+=1
            
            # increment length to check if 
            # queueing has reached its limi
            self.cur_len+=1

        else:
            self.queue.append(data)
            # set rear to new element appended, since list 
            # has different length everytime the enqueue is accessed
            self.rear+=1
            self.cur_len+=1
            
    def dequeue(self):
        if self.isempty():
            print("no elements to delete")

        # when rear and front is equal it 
        # means that it has reached last cel
        elif self.front==self.rear:
            self.front=self.rear=-1

            self.queue.pop(0)
            self.cur_len-=1

        else:
            # set front to the next value
            # of the queue
            self.queue.pop(0)
            self.front+=1
            self.cur_len-=1

    def isfull(self):
        return self.cur_len==self.length
            
    def isempty(self):
        return self.front==-1 and self.rear==-1


def main():
    q=Queue(3)
    print(q.queue)
    print(q.isempty())
    

main()
