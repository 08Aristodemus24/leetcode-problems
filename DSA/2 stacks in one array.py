class DoubleStack:
    def __init__(self,CAP=0):
        self.top1=-1
        self.top2=int(CAP/2)-1 # divide stack into two parts such that top of second stack is max index of first stack
        self.stack=[None]*CAP 
        self.CAP=CAP

    def push1(self,data):
        if self.isFull1():
            print("stack 1 is full")
        else:
            self.top1+=1
            self.stack[self.top1]=data
            print("element pushed")

    def push2(self,data):
        if self.isFull2():
            print("stack 2 is full")
        else:
            self.top2+=1
            self.stack[self.top2]=data
            print("element pushed")

    def pop1(self):
        if self.isEmpty1():
            print("no element popped")
        else:
            self.stack[self.top1]=None
            self.top1-=1
            print("element popped")

    def pop2(self):
        if self.isEmpty2():
            print("no element popped")
        else:
            self.stack[self.top2]=None
            self.top2-=1
            print("element popped")

    def isEmpty1(self):
        return self.top1==-1

    def isEmpty2(self):
        return self.top2==int(self.CAP/2)-1

    def isFull1(self):
        return self.top1==self.top2

    def isFull2(self):
        return self.top2==self.CAP-1

def Main():
    stack=DoubleStack(4) # divide stack into two parts
    stack.push1(1)
    stack.push1(2)

    print(stack.isEmpty2())
    print(stack.stack)

Main()