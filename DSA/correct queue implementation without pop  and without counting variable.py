class CircQueue:
    def __init__(self, CAP=0):
        self.front = -1
        self.rear = -1

        # once queue is created
        # its size will be fixed
        # note 0 times list with element or no element
        # equal to empty list
        self.queue = [None] * CAP
        self.CAP = CAP

    def isEmpty(self):
        return self.front == -1 and self.rear == -1

    def isFull(self):
        return (self.rear + 1) % self.CAP == self.front

    def enQueue(self, data):
        if self.isFull():
            print("queue is full!")
            return
        elif self.front == -1 and self.rear - 1:
            # since front and rear is both -1
            # increase by one or in this case 0
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.CAP
            self.queue[self.rear] = data

    def deQueue(self):
        if self.isEmpty():
            print("no element to delete")
            return 

        # if front and rear are equal
        # queue is down to its last element
        elif self.front == self.rear:
            self.queue[self.front] = None
            self.front = self.rear = -1

        # if front is still not at the position
        # of rear move front one step closer to rear
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.CAP

    def peek(self):
        # return the first element in the queue if queue not empty
        return -1 if self.front == -1 else self.queue[self.front]


if __name__ == "__main__":
    q=CircQueue(3)
    q.enQueue('Just')
    q.enQueue('Do')
    q.enQueue('It')
    q.enQueue(1)
    q.enQueue(1)
    q.deQueue()
    q.deQueue()
    q.deQueue()
    q.enQueue(1)
    q.deQueue()
    q.deQueue()
    print(q.queue)

