class DoubleStack:
    def __init__(self,CAP=0):
        self.CAP=CAP
        self.top1=-1
        self.top2=CAP+1
        self.stack=[None]*CAP
        self.mid=int(CAP/2)-1 # when cap is 0 mid is -1 since no element exists

    def push1(self,data):
        pass

    def push2(self,data):
        pass

    def isEmpty1(self):
        return self.top1==-1

    def isEmpty2(self):
        return self.top2==CAP+1

    def isFull1(self):
        return self.top1==mid # if both tops are one element away from meeting then it is full

    def isFull2(self):
        return self.top2==mid

    def pop1(self):
        pass

    def pop2(self):
        pass


def Main():
    stack=DoubleStack(5) # 5/2=2-1=[mid=1]
