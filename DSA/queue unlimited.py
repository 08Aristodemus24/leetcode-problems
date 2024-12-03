class Queue:
    def __init__(self):
        self.queue=[]
        self.front=-1
        self.rear=-1

    def isEmpty(self):
        return self.front==-1 and self.rear==-1

    def enQueue(self,data):
        if self.front==-1 and self.rear==-1:
            